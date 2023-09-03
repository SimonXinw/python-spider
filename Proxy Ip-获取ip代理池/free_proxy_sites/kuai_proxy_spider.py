# _*_ coding : utf-8 _*_
from lxml import etree
import time
import sys
from tqdm import tqdm


class SpiderKuai():

    def __init__(self, *args, **kwargs):

        kwargs['url'] = 'https://www.kuaidaili.com/free/inha/1/'
        kwargs['headers'] = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }

        super().__init__(**kwargs)

    def pre_parse(self):
        self.parse_urls = [
            'https://www.kuaidaili.com/free/intr/',     # 国内普通代理
            'https://www.kuaidaili.com/free/inha/'      # 国内高匿代理
        ]
        return self.parse_urls

    def parse(self):
        """
        解析代理
        """
        content = self.response.text
        tree = etree.HTML(content)
        proxies_obj = tree.xpath('//div[@id="list"]//tbody/tr')
        proxies = []
        for proxy_obj in proxies_obj:
            dic_ = {
                'ip': proxy_obj.xpath('./td[@data-title="IP"]/text()')[0].strip(),
                'port': proxy_obj.xpath('./td[@data-title="PORT"]/text()')[0].strip(),
                'type': proxy_obj.xpath('./td[@data-title="类型"]/text()')[0].strip(),
                'position': proxy_obj.xpath('./td[@data-title="位置"]/text()')[0].strip(),
                'day': proxy_obj.xpath('./td[@data-title="最后验证时间"]/text()')[0].strip().split(' ')[0]
            }
            if dic_['day'] != self.day:
                break
            proxies.append(dic_)
        return proxies

    def get_all_proxies(self):
        """
        获取所有 proxies
        """
        # 1 先获取所有待采集的 proxy list 页
        self.pre_parse()

        # 2 对每个 proxy 信息页的资源进行解析
        for parse_url in self.parse_urls:
            time.sleep(3)
            self.update_attrs(url=parse_url)
            self.update_response()

            # 3 获取资源页所有的 proxy
            count = 1
            pbar = tqdm(file=sys.stdout, desc='[{}] crawling all pages...'.format(
                self.__class__.__name__))
            while True:
                proxies = self.parse()
                if len(proxies) == 0:
                    break

                self.all_proxies += proxies

                next_page = '{}{}/'.format(parse_url, count+1)
                count += 1
                time.sleep(3)
                self.update_attrs(url=next_page)
                self.update_response()

                pbar.update(1)
            pbar.close()

        return self.all_proxies

    def filter_all_proxies_mp(self):
        """
        测试代理 ip 可用性
        多进程处理
        """
        self.all_proxies_filter = dict()

        pool = ProcessPoolExecutor(max_workers=50)
        all_task = [pool.submit(check_proxy_900cha, proxy)
                    for proxy in self.all_proxies]
        for future in tqdm(as_completed(all_task), total=len(all_task), file=sys.stdout, desc='[{}] checking proxies...'.format(self.__class__.__name__)):
            res, proxy = future.result()
            if res:
                self.all_proxies_filter['{}:{}'.format(
                    proxy['ip'], proxy['port'])] = proxy

        self.all_proxies_filter = self.all_proxies_filter.values()
        return self.all_proxies_filter

    def run(self):
        """
        General spider running logic：
            init -> face page url request -> (resource page collect) -> crawl all proxies -> check proxies' useability -> save
        :return:
        """
        # 1 爬取所有 proxies
        self.all_proxies = self.get_all_proxies()
        print('[{}] 爬取代理数：{}'.format(
            self.__class__.__name__, len(self.all_proxies)))
        # 2 过滤可用代理
        self.all_proxies_filter = self.filter_all_proxies_mp()
        print('[{}] 可用代理数：{}'.format(
            self.__class__.__name__, len(self.all_proxies_filter)))
        # 3 存储可用代理
        # 默认存储路径配置在 config 中，如果想要另存，在子爬虫中重构 run() 方法即可
        self.save_to_txt(os.path.join(useful_ip_file_path,
                         useful_ip_file_name), self.all_proxies_filter)

        print('[{}] run successed.'.format(self.__class__.__name__))

        return list(self.all_proxies_filter)


if __name__ == '__main__':
    spider_kuai = SpiderKuai()
    spider_kuai.run()

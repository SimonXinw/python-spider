# _*_ coding : utf-8 _*_
from lxml import etree
import time
import requests


class SpiderKuai(object):

    def __init__(self, save_file_abs_path, retry_num=None):
        self.name = __class__.__name__

        self.url = 'https://www.kuaidaili.com/free/inha/1/'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }

        self.day = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(time.time())).split(' ')[0].strip()

        self.timeout = 3

        self.all_proxies = []

        self.retry_num =  retry_num or 3

        self.retry_count =  1

        self.save_file_abs_path = save_file_abs_path

    def pre_parse(self):
        self.parse_urls = [
            'https://www.kuaidaili.com/free/inha/1/'      # 国内高匿代理
        ]
        return self.parse_urls

    def parse(self):
        """
        解析代理
        """
        content = self.response.text

        tree = etree.HTML(content)

        proxy_ele_list = tree.xpath('//div[@id="list"]//tbody/tr')

        proxy_list = []

        for proxy_ele in proxy_ele_list:
            proxy_dict = {
                'ip': proxy_ele.xpath('./td[@data-title="IP"]/text()')[0].strip(),
                'port': proxy_ele.xpath('./td[@data-title="PORT"]/text()')[0].strip(),
                'type': proxy_ele.xpath('./td[@data-title="类型"]/text()')[0].strip(),
                'position': proxy_ele.xpath('./td[@data-title="位置"]/text()')[0].strip(),
                'day': proxy_ele.xpath('./td[@data-title="最后验证时间"]/text()')[0].strip().split(' ')[0]
            }
            if proxy_dict['day'] != self.day:
                break

            proxy_list.append(proxy_dict)

        return proxy_list

    def get_response(self):
        try:
            self.response = requests.get(
                self.url, headers=self.headers, timeout=self.timeout)
            
        except Exception as e:
            #  请求限制边界
            if self.retry_count >= self.retry_num:
                print(f'Error: 请求失败，达到超出请求次数 {self.retry_num}')

                return

               
            print(f'Error: 第 {self.retry_count} 次请求失败: 5 秒后进行第 {self.retry_count + 1} 次请求')

            self.retry_count += 1
            
            time.sleep(5)

            self.get_response()


    def get_all_proxies(self):
        """
        获取所有 proxies
        """
        # 1 先获取所有待采集的 proxy list 页
        parse_urls = self.pre_parse()


        # 2 对每个 proxy 信息页的资源进行解析
        for index, parse_url in enumerate(parse_urls):
            self.url = parse_url

            # 第一次不等待
            if index != 0:
                time.sleep(3)
            
            # self.update_attrs(url=parse_url)
            self.get_response()

            proxies = self.parse()
            
            self.all_proxies += proxies

        return self.all_proxies


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
        
        return  self.all_proxies



if __name__ == '__main__':
    config = {
        save_file_abs_path: save_file_abs_path
    }
    spider_kuai = SpiderKuai(**config)
    spider_kuai.run()

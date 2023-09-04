
from lxml import etree  # 使用xpath语法解析
import time
import requests


class SpiderSeo(object):

    def __init__(self, save_file_abs_path=None, retry_num=None):
        self.name = __class__.__name__

        self.url = 'https://proxy.seofangfa.com/'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }

        self.day = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(time.time())).split(' ')[0].strip()

        self.timeout = 3

        self.all_proxies = []

        self.retry_num = retry_num or 3

        self.retry_count = 1

        self.save_file_abs_path = save_file_abs_path

    def get_response(self):
        try:
            self.response = requests.get(
                self.url, headers=self.headers, timeout=self.timeout)

        except Exception as e:
            #  请求限制边界
            if self.retry_count >= self.retry_num:
                print(f'Error: 请求失败，达到超出请求次数 {self.retry_num}')

                return

            print(
                f'Error: 第 {self.retry_count} 次请求失败: 5 秒后进行第 {self.retry_count + 1} 次请求')

            self.retry_count += 1

            time.sleep(5)

            self.get_response()

        return None

    def pre_parse(self):
        self.parse_urls = [
            'https://proxy.seofangfa.com/'
        ]

        return self.parse_urls

    def parse(self):
        """
        解析代理
        """
        if not self.response:
            return

        content = self.response.text
        tree = etree.HTML(content)
        proxies_obj = tree.xpath('//table[@class="table"]/tbody/tr')
        proxies = []
        for proxy_obj in proxies_obj:
            dic_ = {
                'ip': proxy_obj.xpath('./td[1]/text()')[0].strip(),
                'port': proxy_obj.xpath('./td[2]/text()')[0].strip(),
                'position': proxy_obj.xpath('./td[4]/text()')[0].strip(),
                'day': proxy_obj.xpath('./td[5]/text()')[0].strip().split(' ')[0],
            }
            proxies.append(dic_)
        return proxies

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
        General spider running logic:
            init -> face page url request -> (resource page collect) -> crawl all proxies -> check proxies' useability -> save
        :return:
        """
        # 1 爬取所有 proxies
        self.all_proxies = self.get_all_proxies()

        print('[{}] 爬取代理数：{}'.format(
            self.__class__.__name__, len(self.all_proxies)))

        return self.all_proxies


if __name__ == '__main__':

    spider_seo = SpiderSeo()

    spider_seo.run()

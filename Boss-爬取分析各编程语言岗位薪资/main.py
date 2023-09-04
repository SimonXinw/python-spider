# _*_ coding : utf-8 _*_
from lxml import etree
import time
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import PAGE_URL


class BossSpider(object):

    def __init__(self, PAGE_URL):
        self.name = __class__.__name__

        self.base_url = PAGE_URL

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }

        self.day = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(time.time())).split(' ')[0].strip()

        self.timeout = 3

        self.all_proxies = []

        self.retry_count = 1

        driver_options = webdriver.ChromeOptions()  # 谷歌选项

        # 设置为开发者模式，避免被识别
        driver_options.add_experimental_option('excludeSwitches',
                                               ['enable-automation'])

        self.driver = webdriver.Chrome(options=driver_options)

        self.wait = WebDriverWait(self.driver, 2)

    def parse(self):
        """
        解析代理
        """
        content = self.page_source

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

            print(
                f'Error: 第 {self.retry_count} 次请求失败: 5 秒后进行第 {self.retry_count + 1} 次请求')

            self.retry_count += 1

            time.sleep(5)

            self.get_response()

    def run(self):
        """
        General spider running logic：
            init -> face page url request -> (resource page collect) -> crawl all proxies -> check proxies' useability -> save
        :return:
        """
        self.driver.get(self.base_url)

        # 等待 - 页面加载完成，设置最长等待时间为 10 秒
        wait = WebDriverWait(self.driver, 10)

        # 等待 - 元素渲染出来之后取页面 html 数据
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "search-job-result")))

        self.page_source = self.driver.page_source

        #  分析提取 proxy
        proxies = self.parse()

        self.all_proxies += proxies

        self.driver.quit()

        print('[{}] 爬取代理数：{}'.format(
            self.__class__.__name__, len(self.all_proxies)))

        return self.all_proxies


if __name__ == '__main__':
    config_params = {
        "PAGE_URL": PAGE_URL
    }

    instance = BossSpider(**config_params)

    instance.run()

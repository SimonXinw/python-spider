# _*_ coding : utf-8 _*_
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from config import PAGE_URL, CITY_CODE, SEARCH_QUERY, file_abs_path
import time
import requests
import csv
import os


class BossSpider(object):

    def __init__(self, page_url, city, query, save_file_abs_path):
        self.name = __class__.__name__

        # 使用urlencode()将参数编码为URL查询字符串
        params_str = urlencode({'query': query, 'city': city}, safe='')

        self.base_url = page_url + '?' + params_str

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }

        self.day = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(time.time())).split(' ')[0].strip()

        self.timeout = 3

        self.page = 1

        self.save_file_abs_path = save_file_abs_path

        self.all_proxies = []

        self.retry_count = 1

        driver_options = webdriver.ChromeOptions()  # 谷歌选项

        # 设置为开发者模式，避免被识别
        driver_options.add_experimental_option('excludeSwitches',
                                               ['enable-automation'])

        self.driver = webdriver.Chrome(options=driver_options)

        self.wait = WebDriverWait(self.driver, 2)

    def create_csv(self):
        if os.path.isfile(self.save_file_abs_path):
            # 如果文件已存在，直接返回
            print("文件已存在，使用原文件")

            return

        table_header = [
            ["职位名称", "地区", "薪水", "工作年限", '学历', "能力要求", "公司名字", "公司标签",
                "福利待遇", "详情链接"]
        ]

        with open(self.save_file_abs_path, "w", encoding='utf-8-sig', newline="") as file:
            writer = csv.writer(file)

            writer.writerows(table_header)

        print(f"创建成功: 数据已成功写入 => {self.save_file_abs_path}")

    def crawling(self):
        # 等待 - 页面加载完成，设置最长等待时间为 10 秒
        wait = WebDriverWait(self.driver, 10)

        # 等待 - 元素渲染出来之后取页面 html 数据
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "search-job-result")))

        time.sleep(2)

        self.page_source = self.driver.page_source

        self.parse()

        # 保存 csv
        self.save_to_csv()

        self.page = self.page + 1

        time.sleep(2)

        # 查找具有空类名的<a>标签
        a_eles = self.driver.find_elements(
            By.XPATH, '//*[@class="pagination-area"]//a')

        for a_ele in a_eles:
            page_size = a_ele.text.strip()

            if str(self.page) == page_size:
                a_ele.click()

                return

        self.crawling()

    def parse(self):
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(self.page_source, 'html.parser')

        # 找到具有指定类名的<div>标签
        job_results_ele = soup.find('ul', class_='job-list-box')

        job_card_ele_list = job_results_ele.find_all(
            'li', class_='job-card-wrapper')

        job_data_list = []

        # 要按照这个顺序来 ["职位名称", "地区", "薪水", "工作年限", '学历', "能力要求", "公司名字", "公司标签","福利待遇"]

        for job_card_ele in job_card_ele_list:
            job_data = []

            job_body_ele = job_card_ele.find('div',
                                             {'class': 'job-card-body'})

            job_footer_ele = job_card_ele.find('div',
                                               {'class': 'job-card-footer'})

            job_data.append(job_body_ele.find('span',
                                              {'class': 'job-name'}).text.strip())

            job_data.append(job_body_ele.find('span',
                                              {'class': 'job-area-wrapper'}).text.strip())

            job_data.append(job_body_ele.find('span',
                                              {'class': 'salary'}).text.strip())

            job_data.append(job_body_ele.find('ul',
                                              class_='tag-list').find('li').text.strip())

            job_data.append(job_body_ele.find('ul',
                                              class_='tag-list').find_all('li')[1].text.strip())

            job_skill_list = job_footer_ele.find('ul',
                                                 class_='tag-list').find_all('li')
            job_skill = ''

            for skill in job_skill_list:
                job_skill += ',' + skill.text.strip()

            job_data.append(job_skill)

            job_data.append(job_body_ele.find('h3',
                                              class_='company-name').text.strip())

            company_skill_list = job_body_ele.find('ul',
                                                   class_='company-tag-list').find_all('li')
            company_skill = ''

            for skill in company_skill_list:
                company_skill += ',' + skill.text.strip()

            job_data.append(company_skill)

            job_data.append(job_footer_ele.find('div',
                                                {'class': 'info-desc'}).text.strip())

            job_data_list.append(job_data)

        self.job_data_list = job_data_list

        return self.job_data_list

    def save_to_csv(self):
        # 打开已存在的CSV文件，以追加模式打开
        with open(self.save_file_abs_path, 'a', newline='') as file:
            writer = csv.writer(file)

            writer.writerows(self.job_data_list)

            print(f'追加成功: 数量 {len(self.job_data_list)}')

    def run(self):
        """
        General spider running logic：
            init -> face page url request -> (resource page collect) -> crawl all proxies -> check proxies' useability -> save
        :return:
        """
        #  创建一个 csv 表
        self.create_csv()

        self.driver.get(self.base_url)

        self.crawling()

        self.driver.quit()


if __name__ == '__main__':
    config_params = {
        "page_url": PAGE_URL,
        "city": CITY_CODE,
        "query": SEARCH_QUERY,
        "save_file_abs_path": file_abs_path
    }

    instance = BossSpider(**config_params)

    instance.run()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs
from config import SAVE_DIR_PATH, PAGE_URL, DOWNLOAD_IMAGE_NUMBER
import get_detail_urls
import download_images
import get_image_urls


class WebScraper:
    def __init__(self, base_url, save_dir_path, download_number):
        self.base_url = base_url

        self.save_dir_path = save_dir_path

        self.download_number = download_number

    def crawling(self):
        detail_page_urls = []
        page_no = -1

        #  小于要下载的数量的时候要继续下载
        while len(detail_page_urls) < self.download_number:
            page_no = page_no + 1

            page_url = f'http://www.netbian.com/e/search/result/index.php?page=${page_no}&searchid=54'

            res_image_urls = get_detail_urls.get_urls(
                page_url, self.download_number)

            # 存在值，加到数组里面
            if res_image_urls:
                detail_page_urls.extend(res_image_urls)

        #  过滤出对应的数量
        detail_page_urls = detail_page_urls[:20]

        #  请求出指定的图片 url 链接

        image_urls = get_image_urls.get_urls(detail_page_urls)

        if not image_urls:
            return print('抓取失败: >>>>>>>>>> image_url 为空')

        download_images.save_images(image_urls, self.save_dir_path)


scraper = WebScraper(PAGE_URL,
                     SAVE_DIR_PATH, DOWNLOAD_IMAGE_NUMBER)

scraper.crawling()

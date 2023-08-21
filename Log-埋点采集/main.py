from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from spiders.download import save_images
from spiders.get_images import get_menu_item_name
from config import SAVE_DIR_PATH, PAGE_URL, COOKIES


class WebScraper:
    def __init__(self, base_url, save_dir_path):
        self.base_url = base_url

        self.save_dir_path = save_dir_path

        driver_options = webdriver.ChromeOptions()  # 谷歌选项

        # 设置 User-Agent 头
        driver_options.add_argument(
            'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')

        # 设置为开发者模式，避免被识别
        driver_options.add_experimental_option('excludeSwitches',
                                               ['enable-automation'])

        self.driver = webdriver.Chrome(options=driver_options)

        self.wait = WebDriverWait(self.driver, 2)

    def crawling(self):
        self.driver.get(self.base_url)

        # 设置 cookie
        cookies = []

        for cookie in COOKIES.split('; '):
            key, value = cookie.split('=', 1)

            cookies.append({
                "name": key,
                "value": value
            })

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        # 等待页面加载完成，设置最长等待时间为 10 秒
        wait = WebDriverWait(self.driver, 10)

        # 等待元素渲染出来之后取页面 html 数据
        wait.until(EC.presence_of_element_located((By.ID, 'app')))

        html_page_source = self.driver.page_source

        format_title_list = []

        # 指定循环次数
        for i in range(4):
            # 添加进去
            format_title_list = get_menu_item_name(html_page_source)

        self.driver.quit()

        #  返回东西
        format_title_list or []


scraper = WebScraper(PAGE_URL, SAVE_DIR_PATH)

scraper.crawling()

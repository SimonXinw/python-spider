from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from spiders.download_images import save_images
from spiders.get_images import get_product_image_links
from config import SAVE_DIR_PATH, PAGE_URL


class WebScraper:
    def __init__(self, search_term, base_url, save_dir_path):
        self.base_url = base_url

        self.search_term = search_term

        self.save_dir_path = save_dir_path

        driver_options = webdriver.ChromeOptions()  # 谷歌选项

        # 设置为开发者模式，避免被识别
        driver_options.add_experimental_option('excludeSwitches',
                                               ['enable-automation'])

        self.driver = webdriver.Chrome(options=driver_options)

        self.wait = WebDriverWait(self.driver, 2)

    def crawling(self):
        self.driver.get(self.base_url)

        #  获取输入框 dom 节点
        input_edit = self.driver.find_element(By.CSS_SELECTOR, '#key')

        input_edit.clear()

        #  搜索商品
        input_edit.send_keys(self.search_term)

        search_button = self.driver.find_element(
            By.CSS_SELECTOR, '#search > div > div.form > button')

        # 点击搜索
        search_button.click()  # 点击

        # 等待页面加载完成，设置最长等待时间为 10 秒
        wait = WebDriverWait(self.driver, 10)

        # 使用显式等待等待特定条件满足后再继续执行后续操作
        wait.until(EC.url_contains("search"))

        current_page_url = self.driver.current_url

        # 根据 url 请求回来图片链接
        image_links = get_product_image_links(current_page_url)

        # 保存图片
        save_images(image_links, self.save_dir_path)

        self.driver.quit()


# 输入搜索商品
search_term = input("请输入需要搜索的商品名称: ") or '连衣裙'

scraper = WebScraper(search_term, PAGE_URL, SAVE_DIR_PATH)

scraper.crawling()

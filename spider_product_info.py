from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import get_images
from download_images import save_images


class MyWebScraper:
    def __init__(self, search_term, base_url):
        self.base_url = base_url

        self.search_term = search_term

        driver_options = webdriver.ChromeOptions()  # 谷歌选项

    # 设置为开发者模式，避免被识别
        driver_options.add_experimental_option('excludeSwitches',
                                               ['enable-automation'])

        self.driver = webdriver.Chrome(options=driver_options)

        self.wait = WebDriverWait(self.driver, 2)

    def scrape(self):
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

        image_links = get_images.get_product_image_links(current_page_url)

        save_images(image_links)

        self.driver.quit()


# 示例使用
search_term = '裤子'
base_url = 'https://www.jd.com/'  # 这里替换为你要访问的 URL
scraper = MyWebScraper(search_term, base_url)
scraper.scrape()

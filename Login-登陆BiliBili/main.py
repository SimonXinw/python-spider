from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import USER, PAGE_URL, PASSWORD
from utils.common import Utils
from image_loaded import ImageLoaded
from config import img_dir_path
import os
import time


class WebOperator:
    def __init__(self, base_url, user, password):
        self.base_url = base_url

        self.user = user

        self.password = password

        driver_options = webdriver.ChromeOptions()  # 谷歌选项

        # 设置 User-Agent 头
        driver_options.add_argument(
            'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/533.00 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')

        # 设置为开发者模式，避免被识别
        driver_options.add_experimental_option('excludeSwitches',
                                               ['enable-automation'])

        self.driver = webdriver.Chrome(options=driver_options)

        self.wait = WebDriverWait(self.driver, 2)

    def crawling(self):
        self.driver.get(self.base_url)

        # 等待页面加载完成，设置最长等待时间为 10 秒
        wait = WebDriverWait(self.driver, 10)

        # 等待元素渲染出来之后取页面 html 数据
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.go-login-btn')))

        #  获取输入框 dom 节点
        login_btn = self.driver.find_element(By.CSS_SELECTOR, '.go-login-btn')

        login_btn.click()

        # 等待元素渲染出来之后取页面 html 数据
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'login-pwd-wp')))

        # 找到 form__item 元素
        login_wrap_ele = self.driver.find_element(
            By.CLASS_NAME, 'login-pwd-wp')

        # 找到带有指定 placeholder 属性的 input 元素
        user_ele = login_wrap_ele.find_element(
            By.XPATH, './/input[@placeholder="请输入账号"]')

        password_ele = login_wrap_ele.find_element(
            By.XPATH, './/input[@placeholder="请输入密码"]')

        login_btn_ele = login_wrap_ele.find_element(
            By.CLASS_NAME, 'btn_primary')

        user_ele.clear()

        password_ele.clear()

        #  搜索商品
        user_ele.send_keys(self.user)

        password_ele.send_keys(self.password)

        login_btn_ele.click()

        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".geetest_panel:last-child .geetest_panel_box .geetest_panel_next .geetest_widget .geetest_item_img")))

        time.sleep(1)

        # 使用CSS选择器找到目标元素
        geetest_widget_ele = self.driver.find_element(
            By.CSS_SELECTOR,  '.geetest_panel:last-child .geetest_panel_box .geetest_panel_next .geetest_widget')

        code_img_ele = geetest_widget_ele.find_element(
            By.CSS_SELECTOR, '.geetest_item_img')

        # 截取指定元素的图像
        utils_instance = Utils()

        code_img_screenshot = code_img_ele.screenshot_as_png

        utils_instance.save_images(code_img_screenshot,  img_dir_path)

        self.driver.quit()


scraper = WebOperator(PAGE_URL, USER, PASSWORD)

scraper.crawling()

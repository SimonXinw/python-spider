from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import USER, PAGE_URL, PASSWORD, ORDER_IMG_NAME,  CODE_IMG_NAME, code_img_abs_path, order_img_abs_path
from utils.common import Utils
from config import img_dir_path
import os
import time
from orc.chaojiying import Chaojiying_Client


class LoginBiliBili(object):
    def __init__(self, page_url, user, password, img_dir_path):
        self.page_url = page_url

        self.user = user

        self.password = password

        self.img_dir_path = img_dir_path

        self.utils = Utils()

        driver_options = webdriver.ChromeOptions()  # 谷歌选项

        # 设置 User-Agent 头
        driver_options.add_argument(
            'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/533.00 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')

        # 设置为开发者模式，避免被识别
        driver_options.add_experimental_option('excludeSwitches',
                                               ['enable-automation'])

        self.driver = webdriver.Chrome(options=driver_options)

        self.wait = WebDriverWait(self.driver, 2)

    def input_account(self):
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

        time.sleep(1.5)

        login_btn_ele.click()

    def orc_image(self, image_file_path):

        chaojiying = Chaojiying_Client(
            'xw1294600058', 'xinwang1997', '952057')  # 用户中心>>软件ID 生成一个替换 96001

        im = open(image_file_path,
                  'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//

        res = chaojiying.PostPic(im, 9501)

        res_str = res['pic_str']

        sorted_str = self.utils.sort_text_order(res_str)

        return sorted_str

    def screenshot_code_img(self):
        # 使用CSS选择器找到验证码容器
        geetest_widget_ele = self.driver.find_element(
            By.CSS_SELECTOR,  '.geetest_panel:last-child .geetest_panel_box .geetest_panel_next .geetest_widget')

        # 分别抓取元素结点
        text_order_ele = code_img_ele = geetest_widget_ele.find_element(
            By.CSS_SELECTOR, '.geetest_tip_img')

        code_img_ele = geetest_widget_ele.find_element(
            By.CSS_SELECTOR, '.geetest_item_wrap')

        ok_btn = geetest_widget_ele.find_element(
            By.CSS_SELECTOR, '.geetest_commit')

        # 截取指定元素的图像
        utils_instance = Utils()

        code_img_screenshot = code_img_ele.screenshot_as_png

        text_order_screenshot = text_order_ele.screenshot_as_png

        utils_instance.save_images(
            code_img_screenshot,  self.img_dir_path, CODE_IMG_NAME)

        utils_instance.save_images(
            text_order_screenshot,  self.img_dir_path, ORDER_IMG_NAME)

        code_text_list = self.orc_image(code_img_abs_path)

        order_text_list = self.orc_image(order_img_abs_path)

        action = ActionChains(self.driver)

        action.move_to_element(code_img_ele)

        for order_index, order_text in enumerate(order_text_list):
            if order_index == 0:
                time.sleep(1)

            time.sleep(2)
            for code_text in code_text_list:
                if (code_text['text'] == order_text['text']):

                    action.move_by_offset(code_text['x'], code_text['y'])

                    action.click()

                    action.perform()

                    break

    def start(self):
        self.driver.get(self.page_url)

        # 等待 - 页面加载完成，设置最长等待时间为 10 秒
        wait = WebDriverWait(self.driver, 10)

        # 等待 - 元素渲染出来之后取页面 html 数据
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.go-login-btn')))

        #  获取输入框 dom 节点
        login_btn = self.driver.find_element(By.CSS_SELECTOR, '.go-login-btn')

        login_btn.click()

        # 等待 - 元素渲染出来之后取页面 html 数据
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'login-pwd-wp')))

        # 登录
        self.input_account()

        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".geetest_panel:last-child .geetest_panel_box .geetest_panel_next .geetest_widget .geetest_item_img")))

        time.sleep(1)

        # 截图
        self.screenshot_code_img()

        self.driver.quit()


if __name__ == '__main__':
    config_dict = {
        'page_url':  PAGE_URL, 'user': USER, 'password': PASSWORD, 'img_dir_path': img_dir_path
    }

    scraper = LoginBiliBili(**config_dict)

    scraper.start()

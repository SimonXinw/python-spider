# _*_ coding : utf-8 _*_

"""
配置文件
"""
from utils import common
import os

RETRY_LIMIT = 4     # 爬取失败时的重试次数

# 可用 ip 存储文件地址
here_cfg = os.path.dirname(__file__)
useful_ip_file_path = os.path.join(here_cfg, 'proxies_spider_results')
# 可用 ip 存储文件名称
useful_ip_file_name = 'useful_proxies_spiding.txt'

# 网站 URL

utils_instance = common.Utils()

PAGE_URL = 'https://www.bilibili.com/'

USER = 0

PASSWORD = ''

CODE_IMG_NAME = 'code.png'

ORDER_IMG_NAME = 'order.png'


# 获取当前文件夹的绝对路径
current_folder = os.getcwd()

# 获取当前文件夹同级的 output_images 文件夹的绝对路径
img_dir_path = os.path.abspath(os.path.join(
    current_folder, 'Login-登陆BiliBili', 'verification_code_img'))

file_name = utils_instance.get_first_filename(img_dir_path)

# excel 文件绝对路径 path
file_abs_path = os.path.abspath(
    os.path.join(img_dir_path, file_name))

# 验证码文件绝对路径 path
code_img_abs_path = os.path.abspath(
    os.path.join(img_dir_path, CODE_IMG_NAME))

# 验证码的顺序文件绝对路径 path
order_img_abs_path = os.path.abspath(
    os.path.join(img_dir_path, ORDER_IMG_NAME))


# 网站 URL
PAGE_URL = 'https://www.bilibili.com/'

COOKIES = ''

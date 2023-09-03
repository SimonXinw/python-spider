# _*_ coding : utf-8 _*_

"""
配置文件
"""
from utils import common
import os

RETRY_LIMIT = 4     # 爬取失败时的重试次数

utils_instance = common.Utils()

# 获取当前文件夹的绝对路径
current_folder = os.getcwd()

# 获取当前文件夹同级的 output_images 文件夹的绝对路径
save_abs_dir_path = os.path.abspath(os.path.join(
    current_folder, 'Proxy Ip-获取ip代理池', 'proxy_result'))

file_name = 'u'

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

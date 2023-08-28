# 网站 URL
import os
from utils import common

utils_instance = common.Utils()

PAGE_URL = 'https://www.bilibili.com/'

USER = 18270515107

PASSWORD = 'xinwang1997'


# 获取当前文件夹的绝对路径
current_folder = os.getcwd()

# 获取当前文件夹同级的 output_images 文件夹的绝对路径
img_dir_path = os.path.abspath(os.path.join(
    current_folder, 'Login-登陆BiliBili', 'verification_code'))

file_name = utils_instance.get_first_filename(img_dir_path)

# excel 文件绝对路径 path
file_abs_path = os.path.abspath(
    os.path.join(img_dir_path, file_name))

# 网站 URL
PAGE_URL = ''

COOKIES = ''

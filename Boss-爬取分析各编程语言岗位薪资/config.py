# 网站 URL
import os
from utils import common

utils_instance = common.Utils()

PAGE_URL = 'https://www.zhipin.com/web/geek/job?query=%E5%89%8D%E7%AB%AF%E5%B7%A5%E7%A8%8B%E5%B8%88&city=101280600'

SEARCH_QUERY = '前端工程师'


# 获取当前文件夹的绝对路径
current_folder = os.getcwd()

# 获取当前文件夹同级的 output_images 文件夹的绝对路径
img_dir_path = os.path.abspath(os.path.join(
    current_folder, 'Login-登陆BiliBili', 'verification_code_img'))

file_name = utils_instance.get_first_filename(img_dir_path)

# excel 文件绝对路径 path
file_abs_path = os.path.abspath(
    os.path.join(img_dir_path, file_name))

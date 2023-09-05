# 网站 URL
import os
from utils import common

utils_instance = common.Utils()

SEARCH_QUERY = '测试工程师'

CITY_CODE = '101280600'

PAGE_URL = 'https://www.zhipin.com/web/geek/job'


# 获取当前文件夹的绝对路径
current_folder = os.getcwd()

# 获取当前文件夹同级的 output_images 文件夹的绝对路径
img_dir_path = os.path.abspath(os.path.join(
    current_folder, 'Boss-爬取分析各编程语言岗位薪资', 'result_csv'))

file_name = utils_instance.get_first_filename(img_dir_path)

# excel 文件绝对路径 path
file_abs_path = os.path.abspath(
    os.path.join(img_dir_path, file_name))

# 网站 URL
import os
from utils import common

utils_instance = common.Utils()

SEARCH_QUERY = '前端工程师'

CITY_CODE = '101280600'

PAGE_URL = 'https://www.zhipin.com/shenzhen/'

FILE_NAME = 'data.csv'

# 设置代理IP和端口
PROXY_DICT = {
    "ip": '49.234.210.170',
    "port": '3128',
    "user": 'simon',
    "password": 'xinwang'
}

# 获取当前文件夹的绝对路径
current_folder = os.getcwd()

# 获取当前文件夹同级的 output_images 文件夹的绝对路径
dir_path = os.path.abspath(os.path.join(
    current_folder, 'Boss-爬取分析各编程语言岗位薪资', 'result_csv'))

# excel 文件绝对路径 path
file_abs_path = os.path.abspath(
    os.path.join(dir_path, FILE_NAME))

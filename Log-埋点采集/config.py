import os

# 获取当前文件夹的绝对路径
current_folder = os.getcwd()

# 获取当前文件夹同级的 output_images 文件夹的绝对路径
SAVE_DIR_PATH = os.path.abspath(os.path.join(
    current_folder, 'Log-埋点采集', 'output_files'))

# 网站 URL
PAGE_URL = ''

COOKIES = ''

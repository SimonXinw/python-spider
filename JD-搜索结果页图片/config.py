import os

# 获取当前文件夹的绝对路径
current_folder = os.getcwd()

# 获取当前文件夹同级的 output_images 文件夹的绝对路径
SAVE_DIR_PATH = os.path.abspath(os.path.join(
    current_folder, 'JD-搜索结果页图片', 'output_images'))

# 网站 URL
PAGE_URL = 'https://www.jd.com/'

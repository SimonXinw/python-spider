import os
# 获取当前文件夹的绝对路径
current_folder = os.getcwd()

# 获取当前文件夹同级的 output_images 文件夹的绝对路径
SAVE_DIR_PATH = os.path.abspath(os.path.join(
    current_folder, 'BiZhi-下载固定尺寸壁纸', 'output_images'))

PAGE_URL = 'http://www.netbian.com/e/search/result/index.php?page=0&searchid=54'  # 网站根地址

INTERVAL_TIME = 10  # 爬取图片的间隔时间

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'

DOWNLOAD_IMAGE_NUMBER = 20

classificationDict = {}  # 存放网站分类子页面的信息

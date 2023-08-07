# 引入模块
import os
import requests
from utils import common


def download_image(image_url, save_path, index):
    #  兼容 // url 代码

    if image_url.startswith('//'):
        image_url = 'https:' + image_url  # 假设默认使用 http 协议，你可以根据需要更改为 https

    response = requests.get(image_url)

    #  失败直接拒绝
    if response.status_code != 200:
        print(f"失败{index + 1} - 图片\文件路径: >>> {image_url}")
        return None

    with open(save_path, 'wb') as file:
        file.write(response.content)

    print(f"下载{index + 1} - 图片文件路径：>>> {save_path}")


def save_images(image_links, SAVE_DIR_PATH):
    if not image_links:
        print('下载文件失败>>>>>>>>>>>>>>>：空数组')
    else:
        # 检查文件夹是否存在，如果不存在，请创建它
        if not os.path.exists(SAVE_DIR_PATH):
            os.makedirs(SAVE_DIR_PATH)

        for index, image_url in enumerate(image_links):
            # 从URL中提取文件名
            filename = image_url.split("/")[-1]

            # 设置保存图像的路径
            save_file_path = os.path.join(SAVE_DIR_PATH, filename)

            download_image(image_url, save_file_path, index)

        # 判断下载了多少张图片
        success_num = common.get_images(SAVE_DIR_PATH)

        return success_num

# 引入模块
import get_images
import os
import requests

# 请求的网址 URL
page_url = "https://search.jd.com/Search?keyword=%E8%BF%9E%E8%A1%A3%E8%A3%99"

# Folder where you want to save the images
save_dir_path = "/Users/xinwang/Desktop/京东项目/output_images"


def download_image(image_url, save_path):
    #  兼容 // url 代码

    if image_url.startswith('//'):
        image_url = 'https:' + image_url  # 假设默认使用 http 协议，你可以根据需要更改为 https

    response = requests.get(image_url)

    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"下载 - 图片文件路径：>>> {save_path}")
    else:
        print(f"Failed to download the image: {image_url}")


# Check if the folder exists, if not, create it
if not os.path.exists(save_dir_path):
    os.makedirs(save_dir_path)

# 请求图片链接
# image_links = get_images.get_product_image_links(page_url)


def save_images(image_links):
    if not image_links:
        print('下载文件失败>>>>>>>>>>>>>>>：空数组')
    else:
        for image_url in image_links:
            # Extract the filename from the URL
            filename = image_url.split("/")[-1]

        # Set the path to save the image
            save_file_path = os.path.join(save_dir_path, filename)

            download_image(image_url, save_file_path)

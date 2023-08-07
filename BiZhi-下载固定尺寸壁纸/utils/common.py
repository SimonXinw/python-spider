import os


def get_images(folder_path):
    image_extensions = ['.jpg', '.jpeg',
                        '.png', '.gif', '.bmp']  # 支持的图片文件扩展名

    count = 0

    for filename in os.listdir(folder_path):
        extension = os.path.splitext(filename)[1].lower()
        if extension in image_extensions:
            count += 1

    return count

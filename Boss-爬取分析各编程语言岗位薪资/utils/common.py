import os
import re
from PIL import Image


class Utils(object):
    def __init__(self):
        pass

    def get_images(self, folder_path):
        image_extensions = ['.jpg', '.jpeg',
                            '.png', '.gif', '.bmp']  # 支持的图片文件扩展名

        count = 0

        for filename in os.listdir(folder_path):
            extension = os.path.splitext(filename)[1].lower()
            if extension in image_extensions:
                count += 1

        return count

    def save_images(self, image_file, SAVE_DIR_PATH, file_name):

        # 检查文件夹是否存在，如果不存在，请创建它
        if not os.path.exists(SAVE_DIR_PATH):
            os.makedirs(SAVE_DIR_PATH)

        # 设置保存图像的路径
        save_file_path = os.path.join(SAVE_DIR_PATH, file_name)

        with open(save_file_path, 'wb') as file:
            file.write(image_file)

        print(f"保存 - 图片文件路径：>>> {save_file_path}")

    """ 
    识别图片的 width, height

    return width, height
    """

    def get_image_width_and_height(self, image_abs_path):
        image = Image.open(image_abs_path)

        # 获取图片的宽度和高度
        image_width, image_height = image.size

        return [image_width, image_height]

    def get_first_filename(self, abs_path):
        # 获取源目录下的所有文件和文件夹
        dir_list = os.listdir(abs_path)

        # 遍历列表，找到第一个正常的文件名称
        for file_name in dir_list:
            if file_name.startswith('.'):
                continue
            else:
                return file_name

    def sort_text_order(self, text_string):

        text_segments = text_string.split("|")

        result = []

        for text_segment in text_segments:
            text_list = text_segment.split(",")

            if not re.search(r'[123456789一二三四五六七八九]+', text_list[0]):

                item = {'text': text_list[0],
                        'x': text_list[1], 'y': text_list[2]}

                result.append(item)

        result = sorted(result, key=lambda x: int(x['x']))

        return result

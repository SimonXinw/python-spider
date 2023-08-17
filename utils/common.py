import os


class Utils:
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

    def get_first_filename(self, abs_path):
        # 获取源目录下的所有文件和文件夹
        dir_list = os.listdir(abs_path)

        # 遍历列表，找到第一个正常的文件名称
        for file_name in dir_list:
            if not file_name.startswith('.'):
                break
            else:
                return file_name

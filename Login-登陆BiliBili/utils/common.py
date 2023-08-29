import os


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

    def save_images(self, image_file, SAVE_DIR_PATH):

        # 检查文件夹是否存在，如果不存在，请创建它
        if not os.path.exists(SAVE_DIR_PATH):
            os.makedirs(SAVE_DIR_PATH)

        # 设置保存图像的路径
        save_file_path = os.path.join(SAVE_DIR_PATH, '1.png')

        with open(save_file_path, 'wb') as file:
            file.write(image_file)

        print(f"保存 - 图片文件路径：>>> {save_file_path}")

    def get_first_filename(self, abs_path):
        # 获取源目录下的所有文件和文件夹
        dir_list = os.listdir(abs_path)

        # 遍历列表，找到第一个正常的文件名称
        for file_name in dir_list:
            if file_name.startswith('.'):
                continue
            else:
                return file_name

import os

# 获取当前文件夹的绝对路径
current_folder = os.getcwd()

# 获取当前文件夹同级的 output_files 文件夹的绝对路径
SAVE_DIR_PATH = os.path.abspath(os.path.join(
    current_folder, 'Excel-处理转化', 'output_files'))

# 获取当前文件夹同级的 pending_files 文件夹的绝对路径
SOURCE_DIR_PATH = os.path.abspath(os.path.join(
    current_folder, 'Excel-处理转化', 'pending_files'))

import time
import os
import json


def save_to_json(file_abs_path, all_proxies):
    """
    存文件
    """

    # 获取文件夹路径
    folder_path = os.path.dirname(file_abs_path)

    # 如果文件夹不存在，则创建文件夹
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 保存为JSON文件
    with open(file_abs_path, "w") as file:
        json.dump(all_proxies, file)

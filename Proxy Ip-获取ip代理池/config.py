# _*_ coding : utf-8 _*_

"""
配置文件
"""
import os

RETRY_LIMIT = 4     # 爬取失败时的重试次数

# 获取当前文件夹的绝对路径
current_folder = os.getcwd()

# 获取当前文件夹同级的 output_images 文件夹的绝对路径
save_abs_dir_path = os.path.abspath(os.path.join(
    current_folder, 'Proxy Ip-获取ip代理池', 'proxy_ip_result'))

file_name = 'proxy_ip_result.json'

# excel 文件绝对路径 path
save_file_abs_path = os.path.abspath(
    os.path.join(save_abs_dir_path, file_name))

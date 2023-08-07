import socket
import os
from config import DOMAINS


class QueryIp:
    def __init__(self) -> None:
        pass

    def output_hosts(self):
        domains = DOMAINS

        # 获取当前文件夹的绝对路径
        current_folder = os.getcwd()

        # 获取当前文件夹同级的 output_images 文件夹的绝对路径
        SAVE_FILE_PATH = os.path.abspath(os.path.join(
            current_folder, 'IP-获取域名对应的IP', 'hosts.txt'))

        with open(SAVE_FILE_PATH, 'w') as f:
            f.write('# GitHub Start \n')

            for domain in domains:
                ip = socket.gethostbyname(domain)

                print('Querying ip for domain %s' % domain + ':' + ip)

                f.write('%s %s\n' % (ip, domain))

                f.write('\n')

            # 结尾
            f.write('# GitHub End \n')


if __name__ == '__main__':
    query = QueryIp()

    query.output_hosts()

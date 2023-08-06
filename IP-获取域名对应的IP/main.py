import socket
import os


def output_hosts():
    domains = ['github.com',
               'gist.github.com',
               'assets-cdn.github.com',
               'raw.githubusercontent.com',
               'gist.githubusercontent.com',
               'cloud.githubusercontent.com',
               'camo.githubusercontent.com',
               'avatars0.githubusercontent.com',
               'avatars1.githubusercontent.com',
               'avatars2.githubusercontent.com',
               'avatars3.githubusercontent.com',
               'avatars4.githubusercontent.com',
               'avatars5.githubusercontent.com',
               'avatars6.githubusercontent.com',
               'avatars7.githubusercontent.com',
               'avatars8.githubusercontent.com',
               'avatars.githubusercontent.com',
               'github.githubassets.com',
               'user-images.githubusercontent.com',
               'codeload.github.com',
               'favicons.githubusercontent.com',
               'api.github.com'
               ]

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
    output_hosts()

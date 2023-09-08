# _*_ coding : utf-8 _*_

import requests
import threading
from lxml import etree


class CheckProxy(list):

    def __init__(self, proxy_list=None):
        self.pending_proxy_list = proxy_list

    def check_proxy_900cha(self, proxy, timeout=3):
        """
        根据 https://ip.900cha.com/ 返回结果来测试代理的可用性
        :param proxy:
        :param timeout:
        :param realtimeout: 是否实时输出可用代理
        :return:
        """

        url = 'https://ip.900cha.com/'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }

        # proxies = {
        #     'http': '{}:{}'.format(proxy['ip'], proxy['port']),
        #     'https': '{}:{}'.format(proxy['ip'], proxy['port']),
        # }
        proxies = {
            'http': 'http://{}:{}@{}:{}'.format(proxy['user'], proxy['password'], proxy['ip'], proxy['port']),
            'https': 'http://{}:{}@{}:{}'.format(proxy['user'], proxy['password'], proxy['ip'], proxy['port']),
        }

        try:
            response = requests.get(url=url, headers=headers,
                                    proxies=proxies, timeout=timeout)

            tree = etree.HTML(response.text)

            res_ip = tree.xpath(
                '//h3[@class="text-danger mt-2"]')[0].text.strip()

            # 无效
            if res_ip != proxy["ip"]:
                return print(f'代理失败: 使用的是本机 ip => {res_ip}')

            # 有效
            print(f'代理成功: {proxy["ip"]}:{proxy["port"]} 有效！')

            return proxy

        except Exception as e:
            print(
                f'Request Error: {proxy["user"]}:{proxy["password"]}@{proxy["ip"]}:{proxy["port"]} 无效x ')

            return False

    def multiple_check(self, proxy_list):

        # 创建线程列表
        threads = []
        results = []

        # 定义线程执行的函数
        def run_check_proxy(proxy):
            result = self.check_proxy_900cha(proxy)

            results.append(result)

        # 创建并启动线程
        for proxy in proxy_list:
            t = threading.Thread(target=run_check_proxy, args=(proxy,))
            t.start()
            threads.append(t)

        # 等待线程执行完成
        for t in threads:
            t.join()

        valid_proxies = [x for x in results if x]

        return valid_proxies


if __name__ == '__main__':
    instance = CheckProxy()

    # 想单独测试 ip 和端口可以直接修改这里，然后再执行
    instance.check_proxy_900cha(
        {"ip": '49.234.210.170', 'port': '16666', 'user': 'xw', 'password': 'xinwang'})

    # instance.multiple_check([{"ip": '49.234.210.170', 'port': '3128'}])

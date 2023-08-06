import requests
from bs4 import BeautifulSoup


def get_urls(urls):
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        # 初始化图片链接列表
        image_links = []

        for url in urls:
            # 1. 发送 GET 请求获取网页内容
            response = requests.get(url, headers=headers)

            # 2.检查请求是否成功
            if (response.status_code != 200):
                return print(f'请求详情页失败, code:{response.status_code}')

            # 3. 使用 BeautifulSoup 解析 HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # 4. 使用 soup 实例对象直接查找商品列表元素
            main_wrap = soup.find('div', {'id': 'main'})

            image_wrap = main_wrap.find('div', {'class': 'pic'})

            # 6.开始写对应的逻辑
            if image_wrap:
                # 提取 10 个包含商品信息的 div
                image_ele = image_wrap.find('img')

                # 遍历列表，获取 div 里面实际包含 url 信息的 img 和跳转的 a 标签

                image_url = image_ele['src']

                image_links.append(image_url)

        # 7. 结果打印图片链接
        if image_links:
            for i, link in enumerate(image_links, start=1):
                print(f"抓取 - 商品{i}的图片链接：{link}")
        else:
            print("无法获取商品图片链接")

        # 8.返回数据
        return image_links or []

    except requests.exceptions.RequestException as e:
        print(f"请求出现异常: {e}")
        return None

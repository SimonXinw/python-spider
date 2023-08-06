import requests
from bs4 import BeautifulSoup


def get_product_image_links(url):
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        # 1. 发送 GET 请求获取网页内容
        response = requests.get(url, headers=headers)

        # 2.检查请求是否成功
        if (response.status_code != 200):
            return print(f'请求失败，code:{response.status_code}')

        # 3. 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 4. 使用 soup 实例对象直接查找商品列表元素
        product_list_father = soup.find('div', {'id': 'J_goodsList'})

        product_list = product_list_father.find('ul', {'class': 'gl-warp'})

        # 5.初始化图片链接列表
        image_links = []

        # 6.开始写对应的逻辑
        if product_list:
            # 提取 10 个包含商品信息的 div
            products = product_list.find_all('div', {'class': 'gl-i-wrap'})

            # 遍历列表，获取 div 里面实际包含 url 信息的 img 和跳转的 a 标签
            for product in products[1:11]:  # 取前十个商品

                image = product.find('img', {"width": "220"})

                if 'src' in image.attrs:
                    image_links.append(image['src'])
                else:
                    image_links.append(image['data-lazy-img'])

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

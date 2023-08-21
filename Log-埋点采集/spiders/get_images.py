import requests
from bs4 import BeautifulSoup


def get_menu_item_name(html_page_source):
    try:
        # 1. 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(html_page_source, 'html.parser')

        # 2. 使用 soup 实例对象直接查找商品列表元素
        selected_head_dom = soup.select_one(
            '.next-shell-header .next-menu-selectable-single .next-selected a')

        str_1 = selected_head_dom.text + ' - '

        str_2 = ''

        list = []

        asid_ul_dom = soup.select_one(
            '.next-shell-aside .next-menu-selectable-single')

        for li_dom in asid_ul_dom.children:
            #  判断是否有 title 过滤 title，item 没有 title 属性
            if (li_dom['title']):
                str_2 = li_dom['title']

                continue
            # 填入格式化字符串
            list.append({
                '页面名称': str_1 + str_2 + ' - ' + li_dom.children[0].children[0].children[0].text,
                'url': li_dom.children[0].children[0].children[0]['href']
            })

        # 返回数据
        return list or []

    except requests.exceptions.RequestException as e:
        print(f"请求出现异常: {e}")
        return None

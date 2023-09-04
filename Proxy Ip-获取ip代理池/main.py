
from call_chain import proxy_spider_list
from config import save_file_abs_path
from check_proxy import CheckProxy
from save_proxy import save_to_json


if __name__ == '__main__':
    config_params = {"save_file_abs_path": ''}

    config_params['save_file_abs_path'] = save_file_abs_path

    check_instance = CheckProxy()

    # 获取爬虫实例列表
    spider_instance_list = [spider()
                            for spider in proxy_spider_list]
    # 按顺序执行爬取站点获取 proxy ip
    for i, spider in enumerate(spider_instance_list):
        # 1.抓取 proxy
        proxies = spider.run()

        # 2.过滤有效 proxy
        valid_proxies = check_instance.multiple_check(proxies)

        if len(valid_proxies) == 0:
            print(f'{spider.name}: 有效代理 0')

        # 保存 proxy
        save_to_json(save_file_abs_path, valid_proxies)

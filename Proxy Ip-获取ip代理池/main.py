
from free_proxy_sites.kuai_proxy_spider import SpiderKuai
from config import save_file_abs_path


if __name__ == '__main__':
    config_params = {save_file_abs_path: ''}

    config_params['save_file_abs_path'] = save_file_abs_path

    spider = SpiderKuai(save_file_abs_path)

    spider.run()

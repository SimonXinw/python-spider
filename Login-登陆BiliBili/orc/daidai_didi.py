# -*- coding: utf-8 -*-
"""
@Project :demo 
@File    :test_ocr.py
@Author  :lijiawei
@Date    :2021/8/10 8:45 上午 
"""
import ddddocr


def orc_img(img_abs_path):
    ocr = ddddocr.DdddOcr()

    with open(img_abs_path, 'rb') as f:
        image = f.read()

    res = ocr.classification(image)

    return res


orc_img('/Users/xinwang/Desktop/xw/python/python-spider/Login-登陆BiliBili/verification_code_img/order.png')

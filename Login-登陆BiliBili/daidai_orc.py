# -*- coding: utf-8 -*-
"""
@Project :demo 
@File    :test_ocr.py
@Author  :lijiawei
@Date    :2021/8/10 8:45 上午 
"""
import ddddocr
from PIL import Image
from config import file_abs_path
import io


ocr = ddddocr.DdddOcr()

with open(file_abs_path, 'rb') as f:
    image = f.read()

res = ocr.classification(image)

print(res)

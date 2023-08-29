import pytesseract
from PIL import Image
from config import file_abs_path


def ocr_code():

    # open image
    image = Image.open(file_abs_path)
    code = pytesseract.image_to_string(image, lang='chi_sim')
    print('输出字符: ' + code)


ocr_code()

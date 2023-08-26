import pytesseract
from PIL import Image


def ocr_code():

    # open image
    image = Image.open('test.png')
    code = pytesseract.image_to_string(image, lang='chi_sim')
    print(code)

from PIL             import Image
from pyocr.tesseract import image_to_string
from re              import sub

def solve_captcha(image, cropbox=None):
    image = Image.open(image).convert('L')
    if type(cropbox) is tuple:
        image = image.crop(cropbox)
    return sub('[\W]', '', (image_to_string(image) or '').strip())

def solve_image(image, cropbox=None):
    image = Image.open(image).convert('L')
    if type(cropbox) is tuple:
        image = image.crop(cropbox)
    return image_to_string(image)

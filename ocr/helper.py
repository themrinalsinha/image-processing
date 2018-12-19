from re              import sub
from PIL             import Image
from pyocr.tesseract import image_to_string

def extract_text(image, captcha=None, cropbox=None):
    image = Image.open(image).convert('L')
    image = image.crop(cropbox) if cropbox and type(cropbox) is tuple else image
    return sub('[\W]', '', (image_to_string(image) or '').strip()) if captcha else image_to_string(image)

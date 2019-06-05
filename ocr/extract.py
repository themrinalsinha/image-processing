from re              import sub
from PIL             import Image
from pyocr.tesseract import image_to_string

def extract_text(image, is_captcha=False):
    image = (image if not isinstance(image, str) else Image.open(image)).convert('L')
    return sub('[\W]', '', (image_to_string(image) or '').strip()) if is_captcha else image_to_string(image)

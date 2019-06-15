from re              import sub
from PIL             import Image
from pyocr.tesseract import image_to_string

class ExtractImageInfo:

    def extract_text(self, is_captcha=False):
        image = (self.image if not isinstance(self.image, str) else Image.open(self.image)).convert('L')
        return is_captcha and sub('[\W]', '', (image_to_string(image) or '').strip()) or image_to_string(image)

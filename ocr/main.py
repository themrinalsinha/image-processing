from PIL      import Image

from .extract import ExtractImageInfo
from .process import ProcessImageData

class OCR(ExtractImageInfo, ProcessImageData):
    def __init__(self, image):
        self.image = Image.open(image)
        super(OCR, self).__init__(image=self.image)

import matplotlib.pyplot as plt

from PIL import Image
from cv2 import cv2 as cv

def showImage(image, size=(20, 20), title='', window=False):
    plt.figure(figsize=size)
    plt.axis('equal')
    plt.title(title)
    if len(image.shape) == 3:
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        window and Image.fromarray(image).show(title=title) or plt.imshow(image)
    elif len(image.shape) == 2:
        window and Image.fromarray(image).show(title=title) or plt.imshow(image, cmap='gray')

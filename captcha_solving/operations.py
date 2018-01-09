import PIL
import cv2
import numpy as np
from PIL import Image

# Change size of image in same ratio.
def change_size(image, size):
    image    = Image.open(image)
    wpercent = (size / float(image.size[0]))
    h_size   = int((float(image.size[1])*float(wpercent)))
    image    = image.resize((size, h_size), PIL.Image.ANTIALIAS)
    return image

# Makes line thinner.
def image_erosion(image):
    img         = cv2.imread(image, 0)
    kernel      = np.ones((5,5), np.uint8)
    img_erosion = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite('eorde_'+image, img_erosion)
    return

# Makes line thicker.
def image_dilation(image):
    img          = cv2.imread(image, 0)
    kernel       = np.ones((5,5), np.uint8)
    img_dilation = cv2.dilate(img, kernel, iterations=1)
    cv2.imwrite('dilate_'+image, img_dilation)

if __name__ == "__main__":
    main()

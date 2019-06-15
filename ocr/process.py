from PIL import ImageDraw

class ProcessImageData(object):
    def __init__(self, image):
        self.image = image

    def bounding_box(self, mark_image=False):
        pixel_data    = self.image.load()
        width, height = self.image.size

        # finding coordinates of bounding rectangle
        x_min = width
        y_min = height
        x_max = 0
        y_max = 0

        for i in range(width):
            for j in range(height):
                if pixel_data[i, j][0] == 0:
                    # getting corners of bounding rectangel
                    if i < x_min: x_min = i
                    if j < y_min: y_min = j
                    if i > x_max: x_max = i
                    if j > y_max: y_max = j
        coordinates = (x_min, y_min, x_max, y_max)
        if not mark_image:
            return coordinates

        draw = ImageDraw.Draw(self.image)
        draw.rectangle(coordinates, fill=None, outline=(255, 0, 0))
        return self.image

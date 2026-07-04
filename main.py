from image import Image
from png import Png

image = Image(1, 1, [b"\xFF\x00\x00"])

Png.write(image, "red_pixel.png", use_mock=False)
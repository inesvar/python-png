from image import Image
from png import Png

image = Image(8192, 8192, [b"\xFF\x00\x00\x00\xFF\x00" * 4096, b"\x00\xFF\x00\xFF\x00\x00" * 4096] * 4096)

Png.write(image, "checkerboard.png", use_mock=False)
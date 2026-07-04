from image import Image
from png_chunks.png_chunk import PngChunk
import zlib

class IdatChunk(PngChunk):
    def __init__(self, image: Image):
        self.scanlines = image.scanlines

    def chunk_type(self):
        return b"IDAT"
    
    def chunk_data(self):
        data = b""
        for scanline in self.scanlines:
            data += zlib.compress(b"\x00" + scanline)
        return data
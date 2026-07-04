from image import Image
from png_chunks.png_chunk import PngChunk

class IhdrChunk(PngChunk):
    def __init__(self, image: Image):
        self.width = image.width
        self.height = image.height
    
    def chunk_type(self):
        return b"IHDR"
    
    def chunk_data(self):
        width = self.width.to_bytes(4) 
        height = self.height.to_bytes(4)
        bit_depth = b"\x08" # hardcoding 8 bit-depth
        color_type = b"\x02" # hardcoding truecolor
        compression_filter_interlace = b"\x00\x00\x00"

        return width + height + bit_depth + color_type + compression_filter_interlace
from image import Image
from png_chunks.png_chunk import PngChunk

class IendChunk(PngChunk):
    def __init__(self, image: Image):
        pass
    
    def chunk_type(self):
        return b"IEND"

    def chunk_data(self):
        return b""
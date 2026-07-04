from image import Image
from png_chunks.ihdr_chunk import IhdrChunk
from png_chunks.idat_chunk import IdatChunk
from png_chunks.iend_chunk import IendChunk
from file_mock import FileMock

class Png:
    magic_number = b"\x89PNG\r\n\x1a\n"
    critical_chunks = [IhdrChunk, IdatChunk, IendChunk]

    @staticmethod
    def write(image: Image, filename: str, use_mock=False):
        file = FileMock(f"{filename}.txt") if use_mock else open(filename, "wb")
        with file:
            file.write(Png.magic_number)
            for chunk in Png.critical_chunks:
                chunk(image).write(file)
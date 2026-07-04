import zlib

class PngChunk:
    @staticmethod
    def compute_crc(chunk_middle):
        crc = zlib.crc32(chunk_middle)
        return crc.to_bytes(4)

    def write(self, file):
        data = self.chunk_data()
        chunk_middle = self.chunk_type() + data
        crc = PngChunk.compute_crc(chunk_middle)
        chunk_length = len(data).to_bytes(4)
        chunk = chunk_length + chunk_middle + crc

        file.write(chunk)
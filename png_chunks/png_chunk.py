import zlib

class PngChunk:
    @staticmethod
    def to_bytes(value, nb_bytes=1, debug_name="value"):
        try:
            result =  value.to_bytes(nb_bytes)
        except OverflowError:
            # what happens if the size is not writeable on 4 bytes ?
            result =  b"\xFF\xFF\xFF\xFF"
            print(f"Oh no ! The {debug_name} {value} is too big to be written on {nb_bytes} bytes, using {int.from_bytes(result)} instead.")
        finally:
            return result
    
    @staticmethod
    def compute_crc(chunk_middle):
        crc = zlib.crc32(chunk_middle)
        return crc.to_bytes(4)

    def write(self, file):
        data = self.chunk_data()
        chunk_middle = self.chunk_type() + data
        crc = PngChunk.compute_crc(chunk_middle)
        chunk_length = PngChunk.to_bytes(len(data), nb_bytes=4, debug_name="chunk length")
        chunk = chunk_length + chunk_middle + crc

        file.write(chunk)
class FileMock:
    def __init__(self, filename):
        self.file = open(filename, "w")
    
    def write(self, data: bytes):
        self.file.write(data.hex(' '))
        self.file.write("\n")
    
    def close(self):
        self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
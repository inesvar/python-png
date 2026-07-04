class Image:
    def __init__(self, scanlines):
        if len(scanlines) == 0:
            raise ValueError("Expected at least one scanline")
        elif len(scanlines[0]) == 0:
            raise ValueError("Scanlines must not be empty")
        elif len(scanlines[0]) % 3 != 0:
            raise ValueError("Each scanline must contain a multiple of 3 bytes (RGB pixels)")
        
        for scanline in scanlines:
            if len(scanline) != len(scanlines[0]):
                raise ValueError("Expected all scanlines to have equal length")

        self.height = len(scanlines)
        self.width = len(scanlines[0]) // 3
        self.scanlines = scanlines
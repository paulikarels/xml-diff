import unittest
from io import BytesIO
from compression_comparison.lzw.bitio import  BitWriter
from compression_comparison.lzw.lzw import lzw_compress_from_string, lzw_decompress_from_bytes


class TestLZW(unittest.TestCase):

    def setUp(self):
        self.input_text = "this is dog"
        self.compressed_file = BytesIO()
        self.decompressed_file = BytesIO()

    def test_lzw_compress_decompress(self):
        with BitWriter(self.compressed_file) as writer:
            lzw_compress_from_string(self.input_text, writer)
        self.compressed_file.seek(0)
        decompressed_text = []
        lzw_decompress_from_bytes(self.compressed_file, decompressed_text)
        decompressed_text = ''.join(decompressed_text)
        print(f"Not compressed: {self.input_text}")
        print(f"Decompressed: {decompressed_text}")
        self.assertEqual(self.input_text, decompressed_text)

if __name__ == "__main__":
    unittest.main()

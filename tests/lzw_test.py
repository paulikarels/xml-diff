import unittest
import os
from io import BytesIO
from compression_comparison.lzw.bitio import BitWriter, BitReader
from compression_comparison.lzw.lzw import (
    lzw_compress,
    lzw_decompress,
    create_test_bits,
    read_test_bits
)

class TestLZW(unittest.TestCase):

    def setUp(self):
        self.data_folder = "tests/data"
        self.result_folder = "tests/test_results"
        self.test_files = ["empty.txt", "shorter_random_text.txt", "shorter_alice.txt"]
        self.input_text = "this is dog"
        self.compressed_file = BytesIO()
        self.decompressed_file = BytesIO()

        if not os.path.exists(self.result_folder):
            os.makedirs(self.result_folder)

    def test_lzw_compress_decompress_files(self):
        for file_name in self.test_files:
            with self.subTest(file=file_name):
                print(f"Current file in test: {file_name}")
                input_path = os.path.join(self.data_folder, file_name)
                compressed_path = os.path.join(self.result_folder, f"{file_name}_test_result.lzw")
                decompressed_path = os.path.join(self.result_folder, f"{file_name}_test_result_decoded.txt")

                if not os.path.exists(input_path):
                    print(f"File not found: {input_path}")
                    continue

                lzw_compress(input_path, compressed_path)

                lzw_decompress(compressed_path, decompressed_path)

                with open(input_path, "r", encoding="utf8", newline='') as f:
                    original_text = f.read()
                with open(decompressed_path, "r", encoding="utf8", newline='') as f:
                    decompressed_text = f.read()

                self.assertEqual(original_text, decompressed_text)

    def test_create_read_bits(self):
        bit_length = 8
        bit_string = create_test_bits(self.input_text, bit_length)
        result_text = read_test_bits(bit_string, bit_length)
        self.assertEqual(self.input_text, result_text)

if __name__ == "__main__":
    unittest.main()

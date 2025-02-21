import unittest
import os
from comp_compare.lzw.encoding import lzw_encode
from comp_compare.lzw.decoding import lzw_decode

class TestLZW(unittest.TestCase):

    def setUp(self):
        """Set up test cases using actual files."""
        self.data_folder = "tests/data"
        self.result_folder = "tests/test_results"
        self.test_files = [
            "alice.txt",
            "empty.txt",
            "small_text_1MB.txt",
            "random_text.txt"
        ]

        if not os.path.exists(self.result_folder):
            os.makedirs(self.result_folder)

        self.files_content = {}
        for file_name in self.test_files:
            file_path = os.path.join(self.data_folder, file_name)
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    self.files_content[file_name] = f.read()
            else:
                raise FileNotFoundError(f"Test file missing: {file_path}")

    def test_lzw_compress_decompress_files(self):
        """Test compressing and decompressing files to verify data integrity."""
        for file_name in self.test_files:
            with self.subTest(file=file_name):
                input_path = os.path.join(self.data_folder, file_name)
                compressed_path = os.path.join(self.result_folder, f"{file_name}.lzw")
                decompressed_path = os.path.join(self.result_folder, f"{file_name}.decoded")

                lzw_encode(input_path, compressed_path)

                lzw_decode(compressed_path, decompressed_path)

                with open(input_path, "r", encoding="utf-8") as f1, open(decompressed_path, "r", encoding="utf-8") as f2:
                    original_text = f1.read()
                    decompressed_text = f2.read()

                self.assertEqual(original_text, decompressed_text, f"Decompressed text does not match for {file_name}")

    def test_empty_file(self):
        """Test that an empty file remains empty after compression and decompression."""
        file_name = "empty.txt"
        input_path = os.path.join(self.data_folder, file_name)
        compressed_path = os.path.join(self.result_folder, f"{file_name}.lzw")
        decompressed_path = os.path.join(self.result_folder, f"{file_name}.decoded")

        lzw_encode(input_path, compressed_path)
        lzw_decode(compressed_path, decompressed_path)

        with open(decompressed_path, "r", encoding="utf-8") as f:
            decompressed_text = f.read()

        self.assertEqual(decompressed_text, "", "Decompressed empty file should be empty")

if __name__ == "__main__":
    unittest.main()

import unittest
import os
from comp_compare.huffman.encoding import huffman_encoding, huffman_decoding
from comp_compare.huffman.compressor import compress, decompress
from comp_compare.huffman.utils import serialize_tree, deserialize_tree

class HuffmanTest(unittest.TestCase):

    def setUp(self):
        self.text = "this is an example for huffman encoding & coding"
        self.empty_text = ""
        self.complex_text = "Yes, this is dog, another test indeed for huffman"

        self.alice_text = self.load_text_from_file('tests/data/alice.txt')
        self.empty_file_text = self.load_text_from_file('tests/data/empty.txt')
        self.small_text = self.load_text_from_file('tests/data/small_text_1MB.txt')
        self.random_text = self.load_text_from_file('tests/data/random_text.txt')

    def load_text_from_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found.")
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def test_single_character_repeated(self):
        text = "aaaaa"
        root, encoded_text = huffman_encoding(text)
        decoded_text = huffman_decoding(root, encoded_text)
        self.assertEqual(decoded_text, text, "Decoded repeated single character should match original")

    def test_binary_data(self):
        binary_data = bytes([0, 1, 2, 3, 255, 100, 50, 25])
        binary_str = ''.join(map(chr, binary_data))
        root, encoded_text = huffman_encoding(binary_str)
        decoded_text = huffman_decoding(root, encoded_text)
        self.assertEqual(decoded_text, binary_str, "Decoded binary data should match original")

    def test_huffman_encoding_decoding(self):
        root, encoded_text = huffman_encoding(self.text)
        decoded_text = huffman_decoding(root, encoded_text)
        self.assertEqual(decoded_text, self.text, "Decoded text should match the original text")

        small_text = "abc"
        root, encoded_text = huffman_encoding(small_text)
        decoded_text = huffman_decoding(root, encoded_text)
        self.assertEqual(decoded_text, small_text, "Decoded small text should match original small text")

    def test_empty_text(self):
        root, encoded_text = huffman_encoding(self.empty_text)
        decoded_text = huffman_decoding(root, encoded_text)
        self.assertEqual(decoded_text, self.empty_text, "Decoded empty text should be empty")

    def test_alice_text(self):
        root, encoded_text = huffman_encoding(self.alice_text)
        decoded_text = huffman_decoding(root, encoded_text)
        self.assertEqual(decoded_text, self.alice_text, "Decoded Alice text should match the original text")

    def test_random_text(self):
        root, encoded_text = huffman_encoding(self.random_text)
        decoded_text = huffman_decoding(root, encoded_text)
        self.assertEqual(decoded_text, self.random_text, "Decoded random text should match the original text")

    def test_tree_serialization(self):
        root, encoded_text = huffman_encoding(self.text)
        serialized_tree = serialize_tree(root)
        deserialized_tree = deserialize_tree(serialized_tree)
        decoded_text = huffman_decoding(deserialized_tree, encoded_text)
        self.assertEqual(decoded_text, self.text, "Decoded text from deserialized tree should match the original text")

    def test_compression_decompression(self):
        root, encoded_text = huffman_encoding(self.text)
        compressed_data, padding = compress(encoded_text)
        decompressed_data = decompress(compressed_data, padding)
        decoded_text = huffman_decoding(root, decompressed_data)
        self.assertEqual(decoded_text, self.text, "Decoded text after compression and decompression should match the original text")

    def test_empty_input_compression_decompression(self):
        root, encoded_text = huffman_encoding(self.empty_text)
        compressed_data, padding = compress(encoded_text)
        decompressed_data = decompress(compressed_data, padding)
        decoded_text = huffman_decoding(root, decompressed_data)
        self.assertEqual(decoded_text, self.empty_text, "Decoded empty text after compression should be empty")

    def test_invalid_text_for_encoding(self):
        invalid_text = None
        with self.assertRaises(TypeError):
            huffman_encoding(invalid_text)

if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(HuffmanTest))

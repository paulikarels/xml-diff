import unittest
from compression_comparison.huffman.huffman import huffman_encoding, huffman_decoding, Node

class HuffmanTest(unittest.TestCase):
    def setUp(self):
        self.text = "this is an example for huffman encoding & coding"
        self.empty_text = ""
        self.single_char_text = "aaaaaa"
        self.complex_text = "Yes, this is dog, another test indeed for huffman"

    def test_huffman_encoding(self):
        root, encoded_text = huffman_encoding(self.text)
        self.assertIsInstance(root, Node)
        self.assertIsInstance(encoded_text, str)
        self.assertGreater(len(encoded_text), 0)

    def test_huffman_decoding(self):
        root, encoded_text = huffman_encoding(self.text)
        decoded_text = huffman_decoding(root, encoded_text)
        self.assertEqual(decoded_text, self.text)

if __name__ == "__main__":
    unittest.main()
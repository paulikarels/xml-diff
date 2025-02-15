import os
import pytest
from compression_comparison.huffman.huffman import huffman_encoding, huffman_decoding, compress, decompress

@pytest.fixture(scope="function")
def data_folder():
    return "tests/data/performance_data"

@pytest.fixture(scope="function")
def result_folder():
    folder = "tests/test_results"
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

@pytest.fixture(scope="function")
def raw_file_1MB(data_folder):
    file_path = os.path.join(data_folder, "1M.txt")
    if not os.path.exists(file_path):
        pytest.skip(f"File not found: {file_path}")
    return file_path

@pytest.fixture(scope="function")
def raw_file_5MB(data_folder):
    file_path = os.path.join(data_folder, "5M.txt")
    if not os.path.exists(file_path):
        pytest.skip(f"File not found: {file_path}")
    return file_path

def test_huffman_compression_decompression_output_1MB(raw_file_1MB, result_folder):
    with open(raw_file_1MB, 'r', encoding='utf-8') as f:
        text = f.read()
    
    root, encoded_text = huffman_encoding(text)
    compressed_data, padding = compress(encoded_text)
    
    decompressed_data = decompress(compressed_data, padding)
    decoded_text = huffman_decoding(root, decompressed_data)
    
    with open(os.path.join(result_folder, "1MB_text_compressed.hc"), 'wb') as f:
        f.write(compressed_data)
    
    with open(os.path.join(result_folder, "1MB_text_decompressed.txt"), 'w', encoding='utf-8') as f:
        f.write(decoded_text)
    
    assert text == decoded_text, "TExts are not matching with the original file."

def test_huffman_compression_size_5MB(raw_file_5MB, result_folder):
    with open(raw_file_5MB, 'r', encoding='utf-8') as f:
        text = f.read()
    
    _, encoded_text = huffman_encoding(text)
    compressed_data, _ = compress(encoded_text)
    
    compressed_file_path = os.path.join(result_folder, "5MB_text_compressed.hc")
    
    with open(compressed_file_path, 'wb') as f:
        f.write(compressed_data)
    
    original_size = os.path.getsize(raw_file_5MB)
    compressed_size = os.path.getsize(compressed_file_path)
    
    assert compressed_size < original_size, "Compressed file is not  smaller than original file"

if __name__ == "__main__":
    pytest.main()

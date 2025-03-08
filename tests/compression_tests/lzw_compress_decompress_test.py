import os
import pytest
from comp_compare.lzw.encoding import lzw_encode
from comp_compare.lzw.decoding import lzw_decode

@pytest.fixture(scope="function")
def data_folder():
    return "tests/data"

@pytest.fixture(scope="function")
def result_folder():
    folder = "tests/test_results"
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

@pytest.fixture(scope="function")
def raw_file_alice(data_folder):
    file_path = os.path.join(data_folder, "alice.txt")
    if not os.path.exists(file_path):
        pytest.skip(f"File not found: {file_path}")
    return file_path

@pytest.fixture(scope="function")
def raw_file_random(data_folder):
    file_path = os.path.join(data_folder, "random_text.txt")
    if not os.path.exists(file_path):
        pytest.skip(f"File not found: {file_path}")
    return file_path

@pytest.fixture(scope="function")
def raw_file_redundancy(data_folder):
    file_path = os.path.join(data_folder, "redundancy.txt")
    if not os.path.exists(file_path):
        pytest.skip(f"File not found: {file_path}")
    return file_path

@pytest.fixture(scope="function")
def raw_file_1MB(data_folder):
    file_path = os.path.join(data_folder, "small_text_1MB.txt")
    if not os.path.exists(file_path):
        pytest.skip(f"File not found: {file_path}")
    return file_path

def test_lzw_compression_decompression_alice(raw_file_alice, result_folder):
    compress_file_path = os.path.join(result_folder, "alice_compressed.lzw")
    decompress_file_path = os.path.join(result_folder, "alice_decompressed.txt")

    lzw_encode(raw_file_alice, compress_file_path)

    lzw_decode(compress_file_path, decompress_file_path)

    with open(raw_file_alice, 'r', encoding='utf-8') as f:
        original_text = f.read()

    with open(decompress_file_path, 'r', encoding='utf-8') as f:
        decompressed_text = f.read()

    assert original_text == decompressed_text, "The decompressed text does not match the original file."

    original_size = os.path.getsize(raw_file_alice)
    compressed_size = os.path.getsize(compress_file_path)
    print(f" File: {os.path.basename(raw_file_alice)}")
    print(f" Original size: {original_size / 1024:.2f} KB")
    print(f" Compressed size: {compressed_size / 1024:.2f} KB")
    print(f" Compression ratio: {((original_size - compressed_size) / original_size) * 100:.2f}% smaller\n")

def test_lzw_compression_decompression_random(raw_file_random, result_folder):
    compress_file_path = os.path.join(result_folder, "random_compressed.lzw")
    decompress_file_path = os.path.join(result_folder, "random_decompressed.txt")

    lzw_encode(raw_file_random, compress_file_path)

    lzw_decode(compress_file_path, decompress_file_path)

    with open(raw_file_random, 'r', encoding='utf-8') as f:
        original_text = f.read()

    with open(decompress_file_path, 'r', encoding='utf-8') as f:
        decompressed_text = f.read()

    assert original_text == decompressed_text, "The decompressed text does not match the original file."

    original_size = os.path.getsize(raw_file_random)
    compressed_size = os.path.getsize(compress_file_path)
    print(f"File: {os.path.basename(raw_file_random)}")
    print(f" Original size: {original_size / 1024:.2f} KB")
    print(f" Compressed size: {compressed_size / 1024:.2f} KB")
    print(f" Compression ratio: {((original_size - compressed_size) / original_size) * 100:.2f}% smaller\n")

def test_lzw_compression_decompression_redundancy(raw_file_redundancy, result_folder):
    compress_file_path = os.path.join(result_folder, "redundancy_compressed.lzw")
    decompress_file_path = os.path.join(result_folder, "redundancy_decompressed.txt")

    lzw_encode(raw_file_redundancy, compress_file_path)

    lzw_decode(compress_file_path, decompress_file_path)

    with open(raw_file_redundancy, 'r', encoding='utf-8') as f:
        original_text = f.read()

    with open(decompress_file_path, 'r', encoding='utf-8') as f:
        decompressed_text = f.read()

    assert original_text == decompressed_text, "The decompressed text does not match the original file."

    original_size = os.path.getsize(raw_file_redundancy)
    compressed_size = os.path.getsize(compress_file_path)
    print(f"File: {os.path.basename(raw_file_redundancy)}")
    print(f" Original size: {original_size / 1024:.2f} KB")
    print(f" Compressed size: {compressed_size / 1024:.2f} KB")
    print(f" Compression ratio: {((original_size - compressed_size) / original_size) * 100:.2f}% smaller\n")

def test_lzw_compression_decompression_1MB(raw_file_1MB, result_folder):
    compress_file_path = os.path.join(result_folder, "1MB_compressed.lzw")
    decompress_file_path = os.path.join(result_folder, "1MB_decompressed.txt")

    lzw_encode(raw_file_1MB, compress_file_path)

    lzw_decode(compress_file_path, decompress_file_path)

    with open(raw_file_1MB, 'r', encoding='utf-8') as f:
        original_text = f.read()

    with open(decompress_file_path, 'r', encoding='utf-8') as f:
        decompressed_text = f.read()

    assert original_text == decompressed_text, "The decompressed text does not match the original file."

    original_size = os.path.getsize(raw_file_1MB)
    compressed_size = os.path.getsize(compress_file_path)
    print(f"File: {os.path.basename(raw_file_1MB)}")
    print(f" Original size: {original_size / 1024:.2f} KB")
    print(f" Compressed size: {compressed_size / 1024:.2f} KB")
    print(f" Compression ratio: {((original_size - compressed_size) / original_size) * 100:.2f}% smaller\n")

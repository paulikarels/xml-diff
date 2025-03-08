import os
import pytest
from comp_compare.huffman.encoding import huffman_encoding, huffman_decoding
from comp_compare.huffman.compressor import compress
from comp_compare.huffman.utils import deserialize_tree, serialize_tree

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

def test_huffman_compression_alice(raw_file_alice, result_folder):
    file_path = raw_file_alice

    with open(file_path, 'r', encoding='utf-8') as f:
        original_text = f.read()

    root, encoded_text = huffman_encoding(original_text)
    compressed_data, _ = compress(encoded_text)

    compressed_file_path = os.path.join(result_folder, "alice_compressed.hc")
    decompressed_file_path = os.path.join(result_folder, "alice_decompressed.txt")

    with open(compressed_file_path, 'wb') as f:
        f.write(compressed_data)

    serialized_tree = serialize_tree(root)

    deserialized_tree = deserialize_tree(serialized_tree)
    decompressed_text = huffman_decoding(deserialized_tree, encoded_text)

    with open(decompressed_file_path, 'w', encoding='utf-8') as f:
        f.write(decompressed_text)

    with open(decompressed_file_path, 'r', encoding='utf-8') as f:
        decompressed_text = f.read()

    assert original_text == decompressed_text, f"Decompressed text does not match original text for {os.path.basename(file_path)}."

    print(f"File: {os.path.basename(file_path)}")
    print(f" Original size: {os.path.getsize(file_path) / 1024:.2f} KB")
    print(f" Compressed size: {os.path.getsize(compressed_file_path) / 1024:.2f} KB")
    print(f" Compression ratio: {((os.path.getsize(file_path) - os.path.getsize(compressed_file_path)) / os.path.getsize(file_path)) * 100:.2f}% smaller\n")

def test_huffman_compression_random(raw_file_random, result_folder):
    file_path = raw_file_random

    with open(file_path, 'r', encoding='utf-8') as f:
        original_text = f.read()

    root, encoded_text = huffman_encoding(original_text)
    compressed_data, _ = compress(encoded_text)

    compressed_file_path = os.path.join(result_folder, "random_compressed.hc")
    decompressed_file_path = os.path.join(result_folder, "random_decompressed.txt")

    with open(compressed_file_path, 'wb') as f:
        f.write(compressed_data)

    serialized_tree = serialize_tree(root)

    deserialized_tree = deserialize_tree(serialized_tree)
    decompressed_text = huffman_decoding(deserialized_tree, encoded_text)

    with open(decompressed_file_path, 'w', encoding='utf-8') as f:
        f.write(decompressed_text)

    with open(decompressed_file_path, 'r', encoding='utf-8') as f:
        decompressed_text = f.read()

    assert original_text == decompressed_text, f"Decompressed text does not match original text for {os.path.basename(file_path)}."

    print(f"File: {os.path.basename(file_path)}")
    print(f" Original size: {os.path.getsize(file_path) / 1024:.2f} KB")
    print(f" Compressed size: {os.path.getsize(compressed_file_path) / 1024:.2f} KB")
    print(f" Compression ratio: {((os.path.getsize(file_path) - os.path.getsize(compressed_file_path)) / os.path.getsize(file_path)) * 100:.2f}% smaller\n")

def test_huffman_compression_redundancy(raw_file_redundancy, result_folder):
    file_path = raw_file_redundancy

    with open(file_path, 'r', encoding='utf-8') as f:
        original_text = f.read()

    root, encoded_text = huffman_encoding(original_text)
    compressed_data, _ = compress(encoded_text)

    compressed_file_path = os.path.join(result_folder, "redundancy_compressed.hc")
    decompressed_file_path = os.path.join(result_folder, "redundancy_decompressed.txt")

    with open(compressed_file_path, 'wb') as f:
        f.write(compressed_data)

    serialized_tree = serialize_tree(root)

    deserialized_tree = deserialize_tree(serialized_tree)
    decompressed_text = huffman_decoding(deserialized_tree, encoded_text)

    with open(decompressed_file_path, 'w', encoding='utf-8') as f:
        f.write(decompressed_text)

    with open(decompressed_file_path, 'r', encoding='utf-8') as f:
        decompressed_text = f.read()

    assert original_text == decompressed_text, f"Decompressed text does not match original text for {os.path.basename(file_path)}."

    print(f"File: {os.path.basename(file_path)}")
    print(f" Original size: {os.path.getsize(file_path) / 1024:.2f} KB")
    print(f" Compressed size: {os.path.getsize(compressed_file_path) / 1024:.2f} KB")
    print(f" Compression ratio: {((os.path.getsize(file_path) - os.path.getsize(compressed_file_path)) / os.path.getsize(file_path)) * 100:.2f}% smaller\n")

def test_huffman_compression_1MB(raw_file_1MB, result_folder):
    file_path = raw_file_1MB

    with open(file_path, 'r', encoding='utf-8') as f:
        original_text = f.read()

    root, encoded_text = huffman_encoding(original_text)
    compressed_data, _ = compress(encoded_text)

    compressed_file_path = os.path.join(result_folder, "1MB_compressed.hc")
    decompressed_file_path = os.path.join(result_folder, "1MB_decompressed.txt")

    with open(compressed_file_path, 'wb') as f:
        f.write(compressed_data)

    serialized_tree = serialize_tree(root)

    deserialized_tree = deserialize_tree(serialized_tree)
    decompressed_text = huffman_decoding(deserialized_tree, encoded_text)

    with open(decompressed_file_path, 'w', encoding='utf-8') as f:
        f.write(decompressed_text)

    with open(decompressed_file_path, 'r', encoding='utf-8') as f:
        decompressed_text = f.read()

    assert original_text == decompressed_text, f"Decompressed text does not match original text for {os.path.basename(file_path)}."

    print(f"File: {os.path.basename(file_path)}")
    print(f" Original size: {os.path.getsize(file_path) / 1024:.2f} KB")
    print(f" Compressed size: {os.path.getsize(compressed_file_path) / 1024:.2f} KB")
    print(f" Compression ratio: {((os.path.getsize(file_path) - os.path.getsize(compressed_file_path)) / os.path.getsize(file_path)) * 100:.2f}% smaller\n")

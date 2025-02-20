import os
import pytest
from pytest_benchmark.fixture import BenchmarkFixture
from comp_compare.huffman.encoding import huffman_encoding, huffman_decoding

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

@pytest.fixture(scope="function")
def raw_file_10MB(data_folder):
    file_path = os.path.join(data_folder, "10M.txt")
    if not os.path.exists(file_path):
        pytest.skip(f"File not found: {file_path}")
    return file_path

@pytest.fixture(scope="function")
def raw_file_20MB(data_folder):
    file_path = os.path.join(data_folder, "20M.txt")
    if not os.path.exists(file_path):
        pytest.skip(f"File not found: {file_path}")
    return file_path

def test_compression_performance_1MB(benchmark: BenchmarkFixture, raw_file_1MB, result_folder):
    with open(raw_file_1MB, 'r', encoding='utf-8') as f:
        text = f.read()
    benchmark.pedantic(huffman_encoding, args=(text,), rounds=10)

def test_compression_performance_5MB(benchmark: BenchmarkFixture, raw_file_5MB, result_folder):
    with open(raw_file_5MB, 'r', encoding='utf-8') as f:
        text = f.read()
    benchmark.pedantic(huffman_encoding, args=(text,), rounds=10)

def test_compression_performance_10MB(benchmark: BenchmarkFixture, raw_file_10MB, result_folder):
    with open(raw_file_10MB, 'r', encoding='utf-8') as f:
        text = f.read()
    benchmark.pedantic(huffman_encoding, args=(text,), rounds=10)

def test_decompression_performance_1MB(benchmark: BenchmarkFixture, raw_file_1MB, result_folder):
    with open(raw_file_1MB, 'r', encoding='utf-8') as f:
        text = f.read()
    root, encoded_text = huffman_encoding(text)
    benchmark.pedantic(huffman_decoding, args=(root, encoded_text), rounds=10)

def test_decompression_performance_5MB(benchmark: BenchmarkFixture, raw_file_5MB, result_folder):
    with open(raw_file_5MB, 'r', encoding='utf-8') as f:
        text = f.read()
    root, encoded_text = huffman_encoding(text)
    benchmark.pedantic(huffman_decoding, args=(root, encoded_text), rounds=10)

def test_decompression_performance_10MB(benchmark: BenchmarkFixture, raw_file_10MB, result_folder):
    with open(raw_file_10MB, 'r', encoding='utf-8') as f:
        text = f.read()
    root, encoded_text = huffman_encoding(text)
    benchmark.pedantic(huffman_decoding, args=(root, encoded_text), rounds=10)

if __name__ == "__main__":
    pytest.main()
import os
import pytest
from pytest_benchmark.fixture import BenchmarkFixture
from compression_comparison.lzw.lzw_trie import lzw_compress_with_trie, lzw_decompress

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
    compressed_path = os.path.join(result_folder, "1MB_text_compressed_trie.lzw")
    benchmark.pedantic(lzw_compress_with_trie, args=(raw_file_1MB, compressed_path), rounds=1)

def test_decompression_performance_1MB(benchmark: BenchmarkFixture, raw_file_1MB, result_folder):
    compressed_path = os.path.join(result_folder, "1MB_text_compressed_trie.lzw")
    decompressed_path = os.path.join(result_folder, "1MB_text_decompressed_trie.txt")
    lzw_compress_with_trie(raw_file_1MB, compressed_path)
    benchmark.pedantic(lzw_decompress, args=(compressed_path, decompressed_path), rounds=1)




if __name__ == "__main__":
    pytest.main()

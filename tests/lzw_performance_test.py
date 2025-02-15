# TODO: Remove all (the whole testfile) because it is way too slow on the older version?
import os
import pytest
from pytest_benchmark.fixture import BenchmarkFixture
from compression_comparison.lzw.lzw import lzw_compress, lzw_decompress

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


def test_compression_performance_small(benchmark: BenchmarkFixture, raw_file_1MB, result_folder):
    compressed_path = os.path.join(result_folder, "1MB_text_compressed.lzw")
    benchmark.pedantic(lzw_compress, args=(raw_file_1MB, compressed_path), rounds=10)

def test_decompression_performance_small(benchmark: BenchmarkFixture, raw_file_1MB, result_folder):
    compressed_path = os.path.join(result_folder, "1MB_text_compressed.lzw")
    decompressed_path = os.path.join(result_folder, "1MB_text_compressed.txt")
    lzw_compress(raw_file_1MB, compressed_path)
    benchmark.pedantic(lzw_decompress, args=(compressed_path, decompressed_path), rounds=10)

if __name__ == "__main__":
    pytest.main()
import os
import typer
from comp_compare.huffman.encoding import huffman_encoding, huffman_decoding
from comp_compare.huffman.compress import compress as huffman_compress, decompress as huffman_decompress
from comp_compare.huffman.utils import serialize_tree, deserialize_tree
from comp_compare.lzw.lzw import lzw_compress, lzw_decode

app = typer.Typer()

def write_encoded_file(output_path, root, compressed_text, padding):
    """Write the encoded data to a file."""
    with open(output_path, "wb") as f:
        tree_data = serialize_tree(root)
        f.write(tree_data.encode() + b'\n\n')
        f.write(compressed_text)
        f.write(padding.to_bytes(1, 'big'))

def read_compressed_file(target_path):
    """Read the compressed file and return the relevant data."""
    with open(target_path, "rb") as f:
        tree_data_lines = []
        while True:
            line = f.readline().decode().strip()
            if line == "":
                break
            tree_data_lines.append(line)
        tree_data = ''.join(tree_data_lines)
        compressed_text_with_padding = f.read()
        padding = compressed_text_with_padding[-1]
        compressed_text = compressed_text_with_padding[:-1]
    return tree_data, compressed_text, padding

@app.command()
# e for encoding, d for decoding
def comparator(cmd: str, target: str, method: str):
    """
    Command-line interface for encoding and decoding files using Huffman coding or LZW compression.
    """
    data_folder = "data"
    target_path = os.path.join(data_folder, target)

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    if cmd == "e":
        if method == "huffman":
            with open(target_path, "r", encoding="utf8", newline='') as f:
                text = f.read()

            if not text:
                return

            root, encoded_text = huffman_encoding(text)
            compressed_text, padding = huffman_compress(encoded_text)

            enc_file_name = os.path.splitext(os.path.basename(target))[0]
            output_path = os.path.join(data_folder, enc_file_name + ".hc")
            write_encoded_file(output_path, root, compressed_text, padding)

        elif method == "lzw":
            enc_file_name = os.path.splitext(os.path.basename(target))[0]
            output_path = os.path.join(data_folder, enc_file_name + ".lzw")
            lzw_compress(target_path, output_path)

    elif cmd == "d":
        if method == "huffman":
            tree_data, compressed_text, padding = read_compressed_file(target_path)
            root = deserialize_tree(tree_data)
            encoded_text = huffman_decompress(compressed_text, padding)
            decoded_text = huffman_decoding(root, encoded_text)

            enc_file_name = os.path.splitext(os.path.basename(target))[0]
            output_path = os.path.join(data_folder, enc_file_name + "_decoded.txt")
            with open(output_path, "w", encoding="utf8", newline='') as f:
                f.write(decoded_text)

        elif method == "lzw":
            enc_file_name = os.path.splitext(os.path.basename(target))[0]
            output_path = os.path.join(data_folder, enc_file_name + "_decoded.txt")
            lzw_decode(target_path, output_path)

    else:
        print("Please either type 'e' when encoding or 'd' when decoding")

if __name__ == "__main__":
    app()

import os
import typer
from compression_comparison.huffman.huffman import (
    huffman_encoding,
    huffman_decoding,
    compress,
    decompress,
    serialize_tree,
    deserialize_tree
)

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
def comparator(cmd, target):
    """
    Command-line interface for encoding and decoding files using Huffman coding.
    """
    data_folder = "data"
    target_path = os.path.join(data_folder, target)

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    if cmd == "e":
        with open(target_path, "r", encoding="utf8", newline='') as f:
            text = f.read()

        # Empty File
        if not text:
            return

        root, encoded_text = huffman_encoding(text)
        compressed_text, padding = compress(encoded_text)

        enc_file_name  = os.path.splitext(os.path.basename(target))[0]
        output_path = os.path.join(data_folder, enc_file_name  + ".hc")
        write_encoded_file(output_path, root, compressed_text, padding)

    elif cmd == "d":
        tree_data, compressed_text, padding = read_compressed_file(target_path)
        root = deserialize_tree(tree_data)
        encoded_text = decompress(compressed_text, padding)
        decoded_text = huffman_decoding(root, encoded_text)

        enc_file_name  = os.path.splitext(os.path.basename(target))[0]
        output_path = os.path.join(data_folder, enc_file_name  + "_decoded.txt")
        with open(output_path, "w", encoding="utf8", newline='') as f:
            f.write(decoded_text)

    else:
        print("Please either type 'e' when encoding or 'd' when decoding")

if __name__ == "__main__":
    app()

import typer
import os
from compression_comparison.huffman.huffman import huffman_encoding, huffman_decoding, compress, decompress, serialize_tree, deserialize_tree

app = typer.Typer()

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

        encFileName = os.path.splitext(os.path.basename(target))[0]
        output_path = os.path.join(data_folder, encFileName + ".hc")
        with open(output_path, "wb") as f:
            tree_data = serialize_tree(root)
            f.write(tree_data.encode() + b'\n\n') 
            f.write(compressed_text)
            f.write(padding.to_bytes(1, 'big'))

    elif cmd == "d":
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

        root = deserialize_tree(tree_data)
        encoded_text = decompress(compressed_text, padding)
        decoded_text = huffman_decoding(root, encoded_text)

        decFileName = os.path.splitext(os.path.basename(target))[0]
        output_path = os.path.join(data_folder, decFileName + "_decoded.txt")
        with open(output_path, "w", encoding="utf8", newline='') as f:
            f.write(decoded_text)

    else:
        print("Please either type 'e' when encoding or 'd' when decoding")

if __name__ == "__main__":
    app()
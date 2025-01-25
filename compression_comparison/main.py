import typer
import pickle
import os
from compression_comparison.huffman.huffman import huffman_encoding, huffman_decoding, compress, decompress

app = typer.Typer()

@app.command()
# e for encoding, d for decoding
def comparator(cmd: str, target: str):
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
            pickle.dump(root, f)
            pickle.dump(compressed_text, f)
            pickle.dump(padding, f)

    elif cmd == "d":
        with open(target_path, "rb") as f:
            root = pickle.load(f)
            compressed_text = pickle.load(f)
            padding = pickle.load(f)

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
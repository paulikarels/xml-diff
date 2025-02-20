from .tree import build_huffman_tree, Node
from collections import Counter

def build_codes(node, prefix="", codes={}):
    """
    Builds the Huffman codes for each character by traversing the Huffman tree.
    """
    if node is not None:
        if node.value is not None:
            codes[node.value] = prefix
        build_codes(node.left, prefix + "0", codes)
        build_codes(node.right, prefix + "1", codes)
    return codes

def huffman_encoding(text):
    """
    Encodes the given text using Huffman coding.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    if not text:
        return None, ""

    frequency = Counter(text)
    
    if len(frequency) == 1:
        char = next(iter(frequency))
        root = Node(frequency[char], char)
        return root, '0' * len(text)

    root = build_huffman_tree(text)
    codebook = build_codes(root)
    encoded_text = ''.join(codebook[char] for char in text)
    
    return root, encoded_text

def huffman_decoding(root, encoded_text):
    """
    Decodes a given encoded text using the Huffman tree.
    """
    if not encoded_text or root is None:
        return ""

    if root.left is None and root.right is None:
        return root.value * len(encoded_text)

    decoded_text = ""
    current_node = root

    for bit in encoded_text:
        current_node = current_node.left if bit == "0" else current_node.right

        if current_node.left is None and current_node.right is None:
            decoded_text += current_node.value
            current_node = root 

    return decoded_text

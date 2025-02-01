import heapq
from collections import Counter

class Node:
    """
    Represents a node in the Huffman binary tree.
    Nodes have a frequency, value, left and right properties.
    """
    def __init__(self, frequency, value=None, left=None, right=None):
        self.frequency = frequency
        self.value = value
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(text):
    """
    Builds the Huffman tree for the given text.
    
    Args:
        text (str): The input text to be encoded.
    """
    if not text:
        return None

    frequency = Counter(text)
    
    if len(frequency) == 1:
        char = list(frequency.keys())[0]
        return Node(frequency[char], char)

    heap = [Node(freq, char) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.frequency + right.frequency, None, left, right)
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes(node, prefix="", codes={}):
    """
    Builds the Huffman codes for each character by traversing the Huffman tree.

    Args:
        node (Node): The current node in the Huffman tree.
        prefix (str): The current Huffman code prefix.
        codes (dict): The dictionary to store the Huffman codes.
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

    Args:
        text (str): The input text to be encoded.
    """
    
    if not text: 
        return None, ""

    root = build_huffman_tree(text)
    codebook = build_codes(root)
    if len(codebook) == 1:
        char = next(iter(codebook))
        return Node(len(text), char), '0' * len(text)
    
    encoded_text = ''.join(codebook[char] for char in text)

    
    return root, encoded_text

def huffman_decoding(root, encoded_text):
    """
    Decodes a given encoded text using the Huffman tree.

    Args:
        root (Node): The root node of the Huffman tree.
        encoded_text (str): The encoded text to be decoded.
    """
    if not encoded_text:
        return ""

    decoded_text = ""
    current_node = root

    if current_node.left is None and current_node.right is None:
        decoded_text = current_node.value * len(encoded_text)
        return decoded_text

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            decoded_text += current_node.value
            current_node = root

    return decoded_text

def serialize_tree(node):
    """
    Serializes the Huffman tree into a string representation.

    Args:
        node (Node): The root node of the Huffman tree.
    """
    if node is None:
        return ""
    if node.value is not None:
        escaped_value = node.value.replace("\n", "\\n")
        return f"1{escaped_value}"
    return f"0{serialize_tree(node.left)}{serialize_tree(node.right)}"

def deserialize_tree(data):
    """
    Deserializes a string of the Huffman tree back into a tree structure.

    Args:
        data (str): The string representation of the Huffman tree.
    """
    data_iter = iter(data)
    
    def deserialize_helper():
        bit = next(data_iter)
        if bit == "1":
            value = next(data_iter)
            if value == "\\":
                value += next(data_iter)
            if value == "\\n":
                value = "\n"
            return Node(0, value)
        
        left = deserialize_helper()
        right = deserialize_helper()
        return Node(0, None, left, right)

    return deserialize_helper()

def compress(ones_zeros):
    """
    Compresses the binary string into a bytes object.

    Args:
        ones_zeros (str): The binary string to be compressed.
    """
    padding = 8 - len(ones_zeros) % 8
    if padding != 8:
        ones_zeros += '0' * padding
    byte_array = bytearray()
    for i in range(0, len(ones_zeros), 8):
        byte = ones_zeros[i:i+8]
        byte_array.append(int(byte, 2))
    return bytes(byte_array), padding

def decompress(bytesFile, padding):
    """
    Decompresses the bytes object into a binary string.

    Args:
        bytesFile (bytes): The compressed bytes object.
        padding (int): The padding parameter used during compression.
    """
    ones_zeros = ''.join(f'{byte:08b}' for byte in bytesFile)
    if padding != 8:
        ones_zeros = ones_zeros[:-padding]
    return ones_zeros
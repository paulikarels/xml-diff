import os
from compression_comparison.lzw.bitio import BitReader, BitWriter

CHAR_BIT_LEN = 8  
CODE_BIT_LEN = 12
CHAR_SET_LEN = 2 ** CHAR_BIT_LEN
CODE_SET_LEN = 2 ** CODE_BIT_LEN

def build_lzw_dictionary(input_text=None):
    """
    Create the LZW dictionary with all single-character strings.
    """
    dictionary = {chr(i): i for i in range(CHAR_SET_LEN)}
    if input_text:
        unique_chars = set(input_text)
        for char in unique_chars:
            if char not in dictionary:
                dictionary[char] = len(dictionary)
    return dictionary

def longest_prefix_in_dictionary(dictionary, query):
    """
    Finds the longest prefix of the query that exists in the dictionary.

    Args:
        dictionary (dict): The LZW dictionary.
        query (str): The input string to search for the longest prefix.
    """
    length = 0
    for i in range(1, len(query) + 1):
        if query[:i] in dictionary:
            length = i
    return query[:length] if length > 0 else query[0]

# Encoding consist of 5 steps (From Wikipedia) https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch#Encoding
'''
1. Initialize the dictionary to contain all strings of length one.
2. Find the longest string W in the dictionary that matches the current input.
3. Emit the dictionary index for W to output and remove W from the input.
4. Add W followed by the next symbol in the input to the dictionary.
5. Go to Step 2.
'''
def lzw_compress(origin_filepath, compress_filepath):
    """
    Compresses a file with LZW.

    Args:
        origin_filepath (str): The path to the original file to be compressed.
        compress_filepath (str): The path to the output compressed file.
    """
    # Step 1.
    dictionary = build_lzw_dictionary()
    code = CHAR_SET_LEN + 1

    with open(origin_filepath, 'rb') as ori_f, open(compress_filepath, 'wb') as com_f:
        with BitReader(ori_f) as reader, BitWriter(com_f) as writer:
            input = []
            while True:
                ch = reader.read_bits(CHAR_BIT_LEN)
                if not reader.read:
                    break
                input.append(chr(ch))
            input = ''.join(input)

            while len(input) > 0:
                # Step 2.
                W = longest_prefix_in_dictionary(dictionary, input)
                
                # Step 3.
                writer.write_bits(dictionary[W], CODE_BIT_LEN)

                if len(W) < len(input) and code < CODE_SET_LEN:
                    # Step 4.
                    dictionary[input[:len(W) + 1]] = code
                    code += 1
                
                input = input[len(W):]
            
            writer.write_bits(CHAR_SET_LEN, CODE_BIT_LEN)

# Decoding consists of 3 steps (From Wikipedia) https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch#Decoding
'''
1. Initialize the dictionary to contain all strings of length one.
2. Read the next encoded symbol: Is it encoded in the dictionary?
    Yes:
        Emit the corresponding string W to output.
        Concatenate the previous string emitted to output with the first symbol of W. Add this to the dictionary.
    No:
        Concatenate the previous string emitted to output with its first symbol. Call this string V.
        Add V to the dictionary and emit V to output.
3. Repeat Step 2 until end of input string
'''
def lzw_decompress(compress_filepath, origin_filepath):
    """
    Decompresses a file with LZW.

    Args:
        compress_filepath (str): The path to the compressed file.
        origin_filepath (str): The path to the output decompressed file.
    """
    # Step 1.
    dictionary = [chr(i) for i in range(CHAR_SET_LEN)]
    dictionary.append('')

    with open(compress_filepath, 'rb') as com_f, open(origin_filepath, 'wb') as ori_f:
        with BitReader(com_f) as reader, BitWriter(ori_f) as writer:
            codeword = reader.read_bits(CODE_BIT_LEN)
            if codeword != CHAR_SET_LEN:
                val = dictionary[codeword]
                while True:
                    for ch in val:
                        writer.write_bits(ord(ch), CHAR_BIT_LEN)
                    codeword = reader.read_bits(CODE_BIT_LEN)
                    if codeword == CHAR_SET_LEN:
                        break
                    if len(dictionary) == codeword:
                        # Step 2: No
                        s = val + val[0]
                    else:
                        # Step 2: Yes
                        s = dictionary[codeword]
                    if len(dictionary) < CODE_SET_LEN:
                        dictionary.append(val + s[0])
                    val = s

# Methods for testing purposes
def create_test_bits(input_text, bit_length):
    """
    Creates a bit representation of the input text for testing.

    Args:
        input_text (str): The input text to be converted to bits.
        bit_length (int): The bit length for each character.
    """
    bits = []
    for char in input_text:
        bits.append(format(ord(char), f'0{bit_length}b'))
    return ''.join(bits)

def read_test_bits(bit_string, bit_length):
    """
    Reads a bit string and converts it back to text for testing.

    Args:
        bit_string (str): The bit string to be converted back to text.
        bit_length (int): The bit length for each character.
    """
    text = []
    for i in range(0, len(bit_string), bit_length):
        char_bits = bit_string[i:i + bit_length]
        text.append(chr(int(char_bits, 2)))
    return ''.join(text)

import os
from bitio import BitReader, BitWriter

CHAR_BIT_LEN = 8  
CODE_BIT_LEN = 12
CHAR_SET_LEN = 2 ** CHAR_BIT_LEN
CODE_SET_LEN = 2 ** CODE_BIT_LEN

# Encoding consist of 5 steps (From Wikipedia) https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch#Encoding
'''
1. Initialize the dictionary to contain all strings of length one.
2. Find the longest string W in the dictionary that matches the current input.
3. Emit the dictionary index for W to output and remove W from the input.
4. Add W followed by the next symbol in the input to the dictionary.
5. Go to Step 2.
'''
def build_lzw_dictionary():
    dictionary = {chr(i): i for i in range(CHAR_SET_LEN)}
    return dictionary

def longest_prefix_in_dictionary(dictionary, query):
    length = 0
    for i in range(1, len(query) + 1):
        if query[:i] in dictionary:
            length = i
    return query[:length]

def lzw_compress(origin_filepath, compress_filepath):
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
    dictionary = [chr(i) for i in range(CHAR_SET_LEN)]
    dictionary.append('')

    with open(compress_filepath, 'rb') as com_f, open(origin_filepath, 'wb') as ori_f:
        with BitReader(com_f) as reader, BitWriter(ori_f) as writer:
            # Step 1.
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


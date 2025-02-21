from comp_compare.lzw.dictionary import build_lzw_trie
from comp_compare.lzw.constants import CHAR_BIT_LEN, CODE_BIT_LEN, CHAR_SET_LEN, CODE_SET_LEN
from comp_compare.lzw.bitio import BitReader, BitWriter

# Encoding consist of 5 steps (From Wikipedia) https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch#Encoding
'''
1. Initialize the dictionary to contain all strings of length one.
2. Find the longest string W in the dictionary that matches the current input.
3. Emit the dictionary index for W to output and remove W from the input.
4. Add W followed by the next symbol in the input to the dictionary.
5. Go to Step 2.
'''
def lzw_encode(origin_filepath, compress_filepath):
    """
    Compresses a file with LZW using a Trie structure.

    Args:
        origin_filepath (str): The path to the original file to be compressed.
        compress_filepath (str): The path to the output compressed file.
    """
    # Step 1.
    trie = build_lzw_trie()
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
                W = trie.search_longest_prefix(input)
                
                # Step 3.
                node = trie.root
                for char in W:
                    node = node.children[char]
                writer.write_bits(node.code, CODE_BIT_LEN)

                if len(W) < len(input) and code < CODE_SET_LEN:
                    # Step 4.
                    new_sequence = input[:len(W) + 1]
                    trie.insert(new_sequence, code)
                    code += 1
                
                input = input[len(W):]
            
            writer.write_bits(CHAR_SET_LEN, CODE_BIT_LEN)
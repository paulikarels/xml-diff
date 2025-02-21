from comp_compare.lzw.constants import CHAR_BIT_LEN, CODE_BIT_LEN, CHAR_SET_LEN, CODE_SET_LEN
from comp_compare.lzw.bitio import BitReader, BitWriter

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
def lzw_decode(compress_filepath, origin_filepath):
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

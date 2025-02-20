from comp_compare.lzw.bitio import BitReader, BitWriter

CHAR_BIT_LEN = 8  
CODE_BIT_LEN = 12
CHAR_SET_LEN = 2 ** CHAR_BIT_LEN
CODE_SET_LEN = 2 ** CODE_BIT_LEN

class TrieNode:
    def __init__(self):
        """
        Initializes a TrieNode with an empty dictionary of children and no assigned code.
        """
        self.children = {}
        self.code = None

class Trie:
    def __init__(self):
        """
        Initializes a Trie with a root TrieNode and a size counter.
        """
        self.root = TrieNode()
        self.size = 0

    def insert(self, word, code):
        """
        Inserts a word into the Trie with the given code.

        Args:
            word (str): The word to insert.
            code (int): The code to associate with the word.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.code = code
        self.size += 1

    def search_longest_prefix(self, word):
        """
        Searches for the longest prefix of the given word that exists in the Trie.

        Args:
            word (str): The input word to search for.
        
        Returns:
            str: The longest matching prefix found in the Trie.
        """
        node = self.root
        longest_prefix = ""
        current_prefix = ""
        for char in word:
            if char in node.children:
                node = node.children[char]
                current_prefix += char
                if node.code is not None:
                    longest_prefix = current_prefix
            else:
                break
        return longest_prefix

def build_lzw_trie():
    """
    Create the LZW dictionary using a Trie with all single-character strings.
    """
    trie = Trie()
    for i in range(CHAR_SET_LEN):
        trie.insert(chr(i), i)
    return trie

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

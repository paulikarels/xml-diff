from compression_comparison.lzw.bitio import BitReader, BitWriter

CHAR_BIT_LEN = 8  
CODE_BIT_LEN = 12
CHAR_SET_LEN = 2 ** CHAR_BIT_LEN
CODE_SET_LEN = 2 ** CODE_BIT_LEN

class TrieNode:
    def __init__(self):
        self.children = {}
        self.code = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def insert(self, word, code):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.code = code
        self.size += 1

    def search_longest_prefix(self, word):
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
    trie = Trie()
    for i in range(CHAR_SET_LEN):
        trie.insert(chr(i), i)
    return trie

def lzw_compress_with_trie(origin_filepath, compress_filepath):
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
                W = trie.search_longest_prefix(input)
                if not W:
                    raise ValueError(f"NOt found: {input}")
                
                node = trie.root
                for char in W:
                    if char in node.children:
                        node = node.children[char]
                    else:
                        raise KeyError(f" '{W}' not found")
                
                writer.write_bits(node.code, CODE_BIT_LEN)

                if len(W) < len(input) and code < CODE_SET_LEN:
                    new_sequence = input[:len(W) + 1]
                    trie.insert(new_sequence, code)
                    code += 1
                
                input = input[len(W):]
            
            writer.write_bits(CHAR_SET_LEN, CODE_BIT_LEN)



def lzw_decompress(compress_filepath, origin_filepath):
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
                        s = val + val[0]
                    else:
                        s = dictionary[codeword]
                    if len(dictionary) < CODE_SET_LEN:
                        dictionary.append(val + s[0])
                    val = s

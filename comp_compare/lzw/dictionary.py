from comp_compare.lzw.trie import Trie
from comp_compare.lzw.constants import CHAR_SET_LEN

def build_lzw_trie():
    """Creates the LZW dictionary using a Trie with all single-character strings."""
    trie = Trie()
    for i in range(CHAR_SET_LEN):
        trie.insert(chr(i), i)
    return trie

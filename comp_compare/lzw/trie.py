class TrieNode:
    def __init__(self):
        """Initializes a TrieNode with an empty dictionary of children and no assigned code."""
        self.children = {}
        self.code = None

class Trie:
    def __init__(self):
        """Initializes a Trie with a root TrieNode and a size counter."""
        self.root = TrieNode()
        self.size = 0

    def insert(self, word, code):
        """Inserts a word into the Trie with the given code."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.code = code
        self.size += 1

    def search_longest_prefix(self, word):
        """Searches for the longest prefix of the given word that exists in the Trie."""
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

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

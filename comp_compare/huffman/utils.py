from .tree import Node

def serialize_tree(node):
    """
    Serializes the Huffman tree into a string representation.
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
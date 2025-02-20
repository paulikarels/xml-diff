def compress(ones_zeros):
    """
    Compresses the binary string into a bytes object.
    """
    padding = 8 - len(ones_zeros) % 8
    if padding != 8:
        ones_zeros += '0' * padding
    byte_array = bytearray()
    for i in range(0, len(ones_zeros), 8):
        byte = ones_zeros[i:i+8]
        byte_array.append(int(byte, 2))
    return bytes(byte_array), padding

def decompress(bytesFile, padding):
    """
    Decompresses the bytes object into a binary string.
    """
    ones_zeros = ''.join(f'{byte:08b}' for byte in bytesFile)
    if padding != 8:
        ones_zeros = ones_zeros[:-padding]
    return ones_zeros

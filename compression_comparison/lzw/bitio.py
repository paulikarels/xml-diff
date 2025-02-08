# https://stackoverflow.com/questions/10689748/how-to-read-bits-from-a-file/10691412#10691412
class BitReader(object):
    def __init__(self, input_data):
        if isinstance(input_data, bytes):
            self.input = input_data
            self.index = 0
        else:
            self.input = input_data
        self.accumulator = 0
        self.bcount = 0
        self.read = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def read_bit(self):
        if not self.bcount:
            if isinstance(self.input, bytes):
                if self.index < len(self.input):
                    self.accumulator = self.input[self.index]
                    self.index += 1
                    self.bcount = 8
                    self.read = 1
                else:
                    self.read = 0
                    return None
            else:
                a = self.input.read(1)
                if a:
                    self.accumulator = ord(a)
                    self.bcount = 8
                    self.read = len(a)
                else:
                    self.read = 0
                    return None
        rv = (self.accumulator & (1 << (self.bcount - 1))) >> (self.bcount - 1)
        self.bcount -= 1
        return rv

    def read_bits(self, n):
        v = 0
        while n > 0:
            bit = self.read_bit()
            if bit is None:
                break
            v = (v << 1) | bit
            n -= 1
        return v
    
class BitWriter(object):
    def __init__(self, f):
        self.accumulator = 0
        self.bcount = 0
        self.out = f

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()

    def __del__(self):
        try:
            self.flush()
        except ValueError:  
            pass

    def write_bit(self, bit):
        if self.bcount == 8:
            self.flush()
        if bit:
            self.accumulator |= 1 << (7 - self.bcount) 
        self.bcount += 1

    def write_bits(self, bits, n):
        for i in range(n):
            self.write_bit((bits >> (n - i - 1)) & 1)

    def flush(self):
        if self.bcount > 0:
            self.out.write(bytearray([self.accumulator]))
        self.accumulator = 0
        self.bcount = 0

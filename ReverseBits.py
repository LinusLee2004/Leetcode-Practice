class ReverseBits():
    def reverseBits(self, n):
        binary = bin(n)[2:].zfill(32)
        reversed = binary[::-1]
        return int(reversed,2)

test = 43261596
rv = ReverseBits()
print(rv.reverseBits(test))

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            res = res << 1
            bit = n & 1 # get the rightmost bit
            res = res | bit
            n = n >> 1
        return res

        # 1010 initial
        # 0101 rev

    
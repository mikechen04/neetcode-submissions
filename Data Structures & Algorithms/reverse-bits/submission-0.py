class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 31
        while n > 0:
            if n & 1 == 1:
                res += (2 ** power)
            power -= 1
            n = n >> 1
        return res
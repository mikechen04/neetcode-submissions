class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: # base case
            return x

        l = self.mySqrt(x >> 2) << 1
        r = l + 1

        if r ** 2 > x:
            return l
        else:
            return r
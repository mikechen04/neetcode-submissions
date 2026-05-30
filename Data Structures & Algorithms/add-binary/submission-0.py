class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a, 2)
        num_b = int(b, 2)

        res = num_a + num_b
        bin_res = bin(res)[2:]

        return bin_res


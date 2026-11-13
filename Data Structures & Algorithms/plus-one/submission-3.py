class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_joined = int(''.join(map(str, digits)))
        digits_joined += 1

        res = list(map(int, str(digits_joined)))
        return res



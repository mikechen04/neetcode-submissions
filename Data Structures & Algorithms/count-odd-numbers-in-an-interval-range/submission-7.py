class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd = 0
        for num in range(low, high + 1):
            if num & 1:
                odd += 1
        
        return odd
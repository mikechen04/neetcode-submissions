class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if sum(piles) > h:
            return 2
        return 1
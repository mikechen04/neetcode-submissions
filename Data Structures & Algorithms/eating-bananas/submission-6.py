import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            bitch = sum(math.ceil(p / mid) for p in piles)
            if bitch > h:
                l = mid + 1
            else:
                r = mid - 1
        
        return r + 1
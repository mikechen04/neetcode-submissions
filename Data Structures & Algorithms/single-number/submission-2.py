class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        return min(seen, key=seen.get)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        for i in range(len(nums)):
            if seen[num] > 1:
                return True
            else:
                return False

        return False
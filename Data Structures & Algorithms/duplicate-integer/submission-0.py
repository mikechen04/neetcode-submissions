class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        
        counter = set()
        for num in nums:
            if num in counter:
                return True
            counter.add(num)
        
        return False
        
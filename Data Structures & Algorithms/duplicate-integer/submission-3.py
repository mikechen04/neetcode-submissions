class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap with all the numbers
        # put in each element into the hashmap
        # and if the current element is already in the hashmap
        # return false, otherwise return true

        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 1
        
        return False
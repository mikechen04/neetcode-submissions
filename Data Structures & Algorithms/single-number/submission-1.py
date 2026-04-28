class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 0
        hashmap = {}

        # put nums into a hashmap
        # then return the int in the hashmap that only occurs once
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else: 
                hashmap[num] = 1
        
        for key in hashmap:
            if hashmap[key] == 1:
                return key
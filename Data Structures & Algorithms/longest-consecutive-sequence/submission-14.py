class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        sorted_nums = sorted(list(set(nums)))
        count = maxcount = 1
        #print(sorted_nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i]-1 == sorted_nums[i-1]:
                #print(sorted_nums[i-1], sorted_nums[i]-1)
                count += 1
            else:
                if count > maxcount:
                    maxcount = count
                count = 1
        
        if maxcount > count: 
            return maxcount 
        else:
            return count

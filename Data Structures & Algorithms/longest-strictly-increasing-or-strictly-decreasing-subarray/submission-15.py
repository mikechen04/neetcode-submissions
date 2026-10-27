class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = maxcount = 1

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] >= 1: # increasing
                inc, dec = inc + 1, 1 # reset decreasing
            elif nums[i+1] - nums[i] <= -1: # decreasing
                dec, inc = dec + 1, 1 # reset increasing
            else:
                inc = dec = 1 # reset both since its neither
            
            maxcount = max(maxcount, inc, dec) # find the max of each, each iteration
        
        return maxcount

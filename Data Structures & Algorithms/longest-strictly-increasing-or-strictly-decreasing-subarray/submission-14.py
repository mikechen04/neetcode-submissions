class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        icount = dcount = maxcount = 1

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] <= -1:
                dcount += 1
                icount = 1
            elif nums[i+1] - nums[i] >= 1:
                icount += 1
                dcount = 1
            else:
                icount = dcount = 1
                
            maxcount = max(maxcount, icount, dcount)
        return maxcount
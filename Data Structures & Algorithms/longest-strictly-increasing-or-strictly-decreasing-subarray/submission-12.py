class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        icount = dcount = maxcount = 1

        for i in range(0, len(nums) - 1):
            if nums[i + 1] - nums[i] < 0:
                dcount += 1
                icount = 1
            elif nums[i + 1] - nums[i] > 0:
                icount += 1
                dcount = 1
            else:
                if icount > dcount and icount > maxcount:
                    maxcount = icount
                elif dcount > maxcount:
                    maxcount = dcount
                icount = dcount = 1

        if icount > dcount and icount > maxcount:
            maxcount = icount
        elif dcount > maxcount:
            maxcount = dcount

        return maxcount

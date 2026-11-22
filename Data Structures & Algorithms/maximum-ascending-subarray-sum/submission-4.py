class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res, maxres = nums[0], 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                res += nums[i]
            else:
                maxres = max(maxres, res)
                res = nums[i]
        
        return max(maxres, res)
        
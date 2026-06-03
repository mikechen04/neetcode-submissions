class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set(n for n in nums if n > 0))

        if not nums or nums[0] != 1:
            return 1

        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                return nums[i] + 1
        
        return nums[-1] + 1
        
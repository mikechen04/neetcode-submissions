class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, j in enumerate(nums):
            diff = target - nums[i]
            if diff + j == target:
                return [i, j-2]
            seen[diff] = i
        
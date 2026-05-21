class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

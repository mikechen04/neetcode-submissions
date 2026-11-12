class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            if nums[num] in seen:
                seen.append(nums[num])
            else:
                seen[nums[num]] = 1
        
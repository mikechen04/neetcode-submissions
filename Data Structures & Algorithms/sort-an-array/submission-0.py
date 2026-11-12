class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        pivot = nums[len(nums) // 2]

        low = [x for x in nums if x < pivot]
        low = [x for x in nums if x < pivot]
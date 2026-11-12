class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1

        if target in nums:
            return nums.index(target)

        while l <= h:
            mid = (l + h) // 2
            if mid == target:
                return mid
            elif mid < target:
                l = mid + 1
            else:
                h = mid - 1
        
        return l
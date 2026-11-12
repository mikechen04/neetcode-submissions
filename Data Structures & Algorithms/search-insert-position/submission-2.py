class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # ahhhh binary search
        l, h = 0, len(nums) - 1

        if target in nums:
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
        else:
            for i in range(0, len(nums) - 1):
                if nums[i] > target:
                    return i
        
        return l


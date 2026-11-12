class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # ahhhh binary search
        l, h = 0, len(nums)

        if target in nums:
            while mid <= h:
                mid = (l + h) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    h = mid - 1
        else:
            for i in range(0, len(nums) - 1):
                if nums[i] > target:
                    return i

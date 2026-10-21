class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1

        while l < h:
            mid = l + (h - l) // 2
            if nums[mid] < nums[h]: # min is on left side
                h = mid
            elif nums[mid] > nums[h]: # min is on right side
                l = mid + 1
        
        return nums[(l + h) // 2]
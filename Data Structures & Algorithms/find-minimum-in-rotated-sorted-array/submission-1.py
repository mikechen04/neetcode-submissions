class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mid = l + (r - l) // 2

        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] < nums[mid]:
                l = mid
            elif nums[mid] < nums[r]:
                r = mid

        return mid 

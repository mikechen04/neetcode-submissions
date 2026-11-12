class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        if len(nums) == 1 and nums[0] == target:
            return l

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[r]: # on left side
                r = mid + 1
            elif nums[mid] > nums[r]: # on right side
                l = mid
        
        return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        if len(nums) == 1 and nums[0] == target:
            return l

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target or nums[l] == target or nums[r] == target:
                return mid
            elif nums[mid] < nums[r]: # left part
                r = mid
            else: # left part
                l = mid + 1
        
        return -1
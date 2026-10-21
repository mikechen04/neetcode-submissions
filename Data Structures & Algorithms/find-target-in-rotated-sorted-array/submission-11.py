class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] < nums[mid]: # right part
                l = mid + 1
            elif nums[mid] < nums[r]: # left part
                r = mid-1
                
        return -1
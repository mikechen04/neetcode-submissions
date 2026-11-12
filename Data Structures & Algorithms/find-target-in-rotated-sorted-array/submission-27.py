class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] < nums[mid]: # right segment
                l = mid + 1
            elif nums[mid] < nums[r]: # left segment
                r = mid - 1
            else:
                l += 1
        
        return -1
                
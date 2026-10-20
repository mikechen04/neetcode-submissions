class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = l + (r - l) // 2 # conventional binary search
            if nums[r] > nums[mid]: # min is on left side
                r = mid
            elif nums[mid] > nums[r]: # min is on right side
                l = mid + 1
            #else:
            #    ???
        
        return nums[l + (r - l) // 2]
    

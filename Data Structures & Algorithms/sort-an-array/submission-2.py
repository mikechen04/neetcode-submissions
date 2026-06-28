class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums):
            if len(nums) <= 1:
                return nums
            
            pivot = nums[len(nums) // 2]
            left, mid, right = [], [], []

            for num in nums:
                if num < pivot:
                    left.append(num)
                elif num > pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            return quickSort(left) + mid + quickSort(right)
        
        return quickSort(nums)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums) - 1):
            if nums[i] % 2 == 0: # if even
                nums.insert(0, nums.pop(i))
            else:
                nums.append(nums.pop(i))
        
        return nums

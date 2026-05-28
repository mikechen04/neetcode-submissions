class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
 
        for i in range(len(nums)):
            current_product = 1
            for k in range(len(nums)):
                if i != k:
                    current_product *= nums[k]
            output.append(current_product)
        
        return output
            
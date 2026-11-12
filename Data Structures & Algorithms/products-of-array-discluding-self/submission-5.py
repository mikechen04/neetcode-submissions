class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        tmp = None
        l = 0
        for i in range(len(nums)):
            # skips nums[i] and gets the product 
            while l < len(nums):
            # mults the curr value to tmp, skips nums[i] 
            # goes till the end of the array
                if nums[l] != nums[i]:
                    if tmp is None:
                        tmp = nums[l]
                    else:
                        tmp *= nums[l]
                l += 1
            res.append(tmp)
            l, tmp = 0, None
        
        return res



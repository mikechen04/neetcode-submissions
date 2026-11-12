class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        tmp = 1
        l = 0
        for i in range(len(nums)):
            while l < len(nums):
                if l != i:
                    if nums[l] == 0:
                        tmp = nums[l]
                    else:
                        tmp *= nums[l]
                l += 1
            res.append(tmp)
            l, tmp = 0, 1
        
        return res



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = nums[0]
        res = []
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                # skip i, but multiply everything else then append to the res
                if j != i:
                    temp *= nums[j]
            res.append(temp)
        return res

                
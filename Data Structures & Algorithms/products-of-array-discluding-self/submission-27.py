class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp = 1
        tmp_zero = 1
        res = []
        flag = False
        count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                tmp *= nums[i] # getting the prod of everything but the 0s
            else:
                if count > 0:
                    flag = True
                count += 1
            tmp_zero *= nums[i] # results in 0 if there is a 0 in the array

        for num in nums:
            if num == 0 and flag == False:
                res.append(int(tmp))
            elif num != 0 and flag == False:
                res.append(int(tmp_zero/num))
            else:
                res.append(0)
        
        return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            j, k = 0, len(nums)-1
            target = -nums[i]
            if nums[j] + nums[k] < target:
                j += 1
            elif nums[j] + nums[k] > target:
                k -= 1
            elif nums[j] + nums[k] == target:
                res.append([i, j, k])
                while j < k:
                    j += 1
        
        return res
        

            

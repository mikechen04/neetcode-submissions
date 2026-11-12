class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        j, k = 0, len(nums)-1
        #j = 0
        for i in range(len(nums)):
            k = i-1
            #nums[i] = -(nums[j] + nums[k])
            target = -nums[i]
            if nums[j] + nums[k] < target:
                j += 1
            elif nums[j] + nums[k] > target:
                k -= 1
            elif nums[j] + nums[k] == target:
                tmp = [nums[i], nums[j], nums[k]]
                sort_tmp = sorted(tmp)
                if not any(sorted(item) == sort_tmp for item in res):
                    res.append(tmp)
            
            while j < k:
                j += 1
        
        return res
        

            

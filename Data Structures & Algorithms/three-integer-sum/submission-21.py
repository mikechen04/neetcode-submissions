class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
                j, k = i+1, len(nums)-1
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                while j < k:
                    target = -nums[i]
                    if nums[j] + nums[k] == target:
                        if [nums[i], nums[j], nums[k]] not in res:
                            res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                    elif nums[j] + nums[k] < target:
                        j += 1
                    elif nums[j] + nums[k] > target:
                        k -= 1
            
        return res
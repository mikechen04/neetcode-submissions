class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                # nums[i] = -(nums[j] + nums[k])
                target = -nums[i]
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] == target:
                    tmp = [nums[i], nums[j], nums[k]]
                    sorted_tmp = sorted(tmp)
                    if not any(sorted(item) == sorted_tmp for item in res):
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        
        return res
        

            

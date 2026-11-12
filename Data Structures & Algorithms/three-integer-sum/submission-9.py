class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        tmp_count = sorted(tmp)
                        if not any(sorted(item) == tmp_count for item in res):
                            res.append([nums[i], nums[j], nums[k]])
        
        return res
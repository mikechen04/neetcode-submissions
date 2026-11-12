class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        while nums:
            for i in range(len(nums) - 1):
                if nums[i] + 1 != nums[i+1]:
                    ans.append(nums[i])
                    if nums[i] + 1 > nums[i+1]:
                        ans.append(nums[i] + 1)
                    else:
                        ans.append(nums[i] - 1)
                    return ans
        
        # return ans

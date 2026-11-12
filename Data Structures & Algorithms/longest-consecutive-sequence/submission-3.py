class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = 0
        maxc = 0
        nums.sort()
        unique = set(nums)
        numss = list(unique)
        
        for i in range(len(numss)-1):
            if numss[i+1] == numss[i]+1:
                count += 1
            else:
                if count > maxc:
                    maxc = count
                count = 1
        
        if count > maxc:
            maxc = count
        
        return maxc+1
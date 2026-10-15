class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = 0
        maxc = 0
        unique = set(nums)
        numss = list(unique)
        numss.sort()
        
        for i in range(len(numss)-1):
            if numss[i+1] == numss[i]+1:
                count += 1
            else:
                if count > maxc:
                    maxc = count
                count = 0
        
        if count > maxc:
            maxc = count
        
        return maxc+1
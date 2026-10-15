class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0 
        maxc = 0
        nums.sort()
        unique = list(OrderedDict.fromkeys(nums))

        if not nums:
            return 0

        for i in range(0, len(unique)-1):
            if unique[i+1] == unique[i]+1:
                count += 1
            else:
                if count > maxc:
                    maxc = count
                count = 0
        
        if count > maxc:
            maxc = count
        
        return maxc + 1
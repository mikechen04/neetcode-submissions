class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        res = []
        for i in range(k):
            res.append(max(seen, key=seen.get))
            del seen[max(seen, key=seen.get)]# = -1
        
        #print(seen)
        return res
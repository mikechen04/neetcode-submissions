class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        nums.reverse()

        nums_set = list(set(nums))
        res = []
        for i in range(k):
            res.append(nums_set[i])
        
        return res
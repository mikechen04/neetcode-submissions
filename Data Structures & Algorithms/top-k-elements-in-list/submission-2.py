class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so it asking to return the top k frequent letters
        # so if its 2, and array is 1 2 2 3 3 3, it will return 2 3 
        # since 3 is most frequent, 2 is second most frequent

        # maybe something like a counter? or a hashmap, probably a hashmap
        # then we just need to append the key part instead of key value into a result array

        seen = {}
        res = []
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        fuckyou = sorted(seen.items(), key=lambda pair: pair[1], reverse=True)
        
        for i in range(k):
            res.append(fuckyou[i][0])
        
        return res
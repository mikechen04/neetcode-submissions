class Solution:
    def findLucky(self, arr: List[int]) -> int:
        seen = {}
        for num in arr:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        lucky = []
        for num, count in seen.items():
            if num == count:
                lucky.append(num)
        
        if lucky:
            return max(lucky)
        else:
            return -1
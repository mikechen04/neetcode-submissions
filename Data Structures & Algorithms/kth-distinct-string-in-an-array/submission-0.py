class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        for s in arr:
            if s in seen:
                seen[s] += 1
            else:
                seen[s] = 1
        
        unique = []
        for i in range(len(arr)):
            if seen[arr[i]] == 1:
                unique.append(arr[i])
        
        if k > len(unique):
            return "" 
            
        return unique[k - 1]
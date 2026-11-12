class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l = maxcount = 0

        for r in range(len(s)):
            if s[r] not in visited:
                visited.add(s[r])
            else:
                if len(visited) > maxcount:
                    maxcount = len(visited)
                    l -= 1
                while s[r] in visited:
                    l += 1
                    if s[l] in visited:
                        visited.remove(s[l])
        
        return maxcount
                

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l = count = maxcount = 0

        for r in range(len(s)):
            if s[r] not in visited:
                visited.add(s[r])
                count += 1
            else:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1
                    if s[r] not in visited:
                        visited.add(s[r])
                        break
                if count > maxcount:
                    maxcount = count
                count = r - l + 1

        if count > maxcount:
            maxcount = count
        return maxcount
                

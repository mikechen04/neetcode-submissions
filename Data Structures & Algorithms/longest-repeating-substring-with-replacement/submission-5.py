class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l = 0

        for r in range(len(s)):
            if s[r] in seen:
                seen[s[r]] += 1
            else:
                seen[s[r]] = 1
            
            if (r-l+1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
        
        return (r - l + 1)
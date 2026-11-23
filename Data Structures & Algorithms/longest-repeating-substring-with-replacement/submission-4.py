class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        seen = {}

        for r in range(len(s)):
            if s[r] in seen:  
                seen[s[r]] += 1
            else:
                seen[s[r]] = 1

            if k < (r-l+1) - max(seen.values()):  
                seen[s[l]] -= 1
                l += 1

        return (r - l + 1)
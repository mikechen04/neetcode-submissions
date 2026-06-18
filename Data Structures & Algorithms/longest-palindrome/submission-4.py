class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        res = 0

        for char in s:
            if char in seen:
                seen.remove(char)
                res += 2
            else:
                seen.add(char)
        
        if seen:
            return res + 1
        else:
            return res
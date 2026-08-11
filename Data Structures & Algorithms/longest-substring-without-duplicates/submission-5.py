class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        max_chars = 0

        for r in range(len(s)):
            if s[r] in chars:
                if len(chars) > max_chars: 
                    max_chars = len(chars)
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
            chars.add(s[r])
            
        if len(chars) > max_chars: # update only if its bigger than current max
            max_chars = len(chars)

        if max_chars == 0:
            return len(s)
        else:
            return max_chars
            
        
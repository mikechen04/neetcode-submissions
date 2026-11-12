class Solution:
    def validPalindrome(self, s: str) -> bool:
        s.lower()
        s = ''.join(char for char in s if s.isalnum())
        l, r = 0, len(s)-1
        c = 0
        

        while l <= r:
            if s[l] != s[r]:
                if c == 0:
                    c += 1
                    r += 1
                elif c > 0:
                    return False
            else:
                l += 1
                r -= 1
        
        return True
                
                
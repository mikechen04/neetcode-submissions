class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def helper(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        while l <= r:
            if s[l] != s[r]:
                if helper(s, l+1, r) == True or helper(s, l, r-1) == True:
                    return True
                else:
                    return False
            l += 1
            r -= 1

        return True
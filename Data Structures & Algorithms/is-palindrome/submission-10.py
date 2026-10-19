class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join(char for char in s if char.isalnum())
        sss = ss.lower()

        l, r = 0, len(sss)-1
        while l <= r:
            if sss[l] == sss[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        l, r = 0, len(s) - 1
        mid = len(s) // 2

        while l != mid and r != mid:
            if s[l] != s[r]:
                return True
            l += 1
            r -= 1
        return False

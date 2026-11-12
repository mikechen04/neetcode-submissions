class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if s.isalnum())
        l, r = 1, len(s) - 1
        mid = len(s) // 2

        while l <= mid:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

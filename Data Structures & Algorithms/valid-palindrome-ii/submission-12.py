class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        mismatch = 0

        if len(s) % 2 == 1:
            mismatch += 1

        while l <= r:
            if s[l] != s[r]:
                mismatch += 1
            l += 1
            r -= 1

        if mismatch <= 1:
            return True
        else:
            return False
class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = ""
        for c in s:
            if c.isalnum():
                result += c.lower()
        s = result

        return s == s[::-1]
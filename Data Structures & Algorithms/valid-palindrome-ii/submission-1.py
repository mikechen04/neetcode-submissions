class Solution:
    def validPalindrome(self, s: str) -> bool:
        s.lower()

        if s == s[::-1]:
            return True

        for string in range(len(s)):
            new_string = s[:string] + s[string + 1:]
            if new_string == new_string[::-1]:
                return True

        return False

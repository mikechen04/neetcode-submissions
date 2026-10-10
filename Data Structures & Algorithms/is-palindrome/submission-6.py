class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = s.replace(" ", "")
        sss = "".join(char for char in ss if char.isalnum())
        ssss = sss.lower()
        l, r = 0, len(ssss) - 1

        while l < r:
            if ssss[l] != ssss[r]:
                return False
            l += 1
            r -= 1
        
        return True
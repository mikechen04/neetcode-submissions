class Solution:
    def isPalindrome(self, x: int) -> bool:
        meow = str(x)
        l, r = 0, len(meow) - 1

        while l < r:
            if meow[l] == meow[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
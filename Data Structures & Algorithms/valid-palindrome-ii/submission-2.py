class Solution:
    def validPalindrome(self, s: str) -> bool:
        # lets put everything into a counter
        # if there is one count with count 1, return True
        # if there is 0 counts with count 1, and one with count 2, return True
        # else return False 

        count = Counter(s)

        return count
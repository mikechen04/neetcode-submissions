class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        if len(word1) < len(word2):
            r = len(word2) - 1
        else:
            r = len(word1) - 1

        l = 0
        while l <= r:
            if word1[l]:
                res += word1[l] 
            if word2[l]:
                res += word2[l]
            l += 1
        
        return res
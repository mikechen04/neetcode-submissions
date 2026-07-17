class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        if len(word1) < len(word2):
            r = len(word2) - 1
        else:
            r = len(word1) - 1

        l = 0
        while l <= r:
            if l < len(word1):
                res += word1[l] 
            if l < len(word2):
                res += word2[l]
            l += 1
        
        return res
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        res = ""
        short = min(len(word1), len(word2))
        for i in range(short):
            res += word1[l]
            res += word2[l]
            l += 1
        
        if len(word2) > len(word1):
            r = len(word2) - l-1
            res += word2[r-1:]
        elif len(word1) > len(word2):
            r = len(word1) - l
            res += word1[r-1:]

        return res
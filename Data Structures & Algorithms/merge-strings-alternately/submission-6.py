class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        res = ""
        short = min(len(word1), len(word2))

        for i in range(short):
            res += word1[l]
            res += word2[l]
            l += 1
        
        if len(word1) > len(word2):
            res += word1[l:]
        elif len(word2) > len(word1):
            res += word2[l:]

        return res
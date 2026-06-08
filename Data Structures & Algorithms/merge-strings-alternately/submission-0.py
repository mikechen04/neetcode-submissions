class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0

        if not word1:
            return word2
        elif not word2:
            return word1
        elif not word1 and not word2:
            return res

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
            i += 1
            
        return res
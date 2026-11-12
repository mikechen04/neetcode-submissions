class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for c in range(len(strs[0])):
            char = strs[0][c]
            for i in range(1, len(strs)):
                if c <= len(strs[i]):
                    if strs[i][c] != char:
                        return res
                    else:
                        char = strs[0][c]

            res += char
        
        return res

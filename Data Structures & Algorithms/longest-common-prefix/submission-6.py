class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for c in range(len(strs[0])):
            char = strs[0][c]
            for i in range(1, len(strs)):
                if strs[i][c] != char:
                    return res
                else:
                    if c >= len(strs[i]):
                        char = strs[0][c]

            res += char
        
        return res

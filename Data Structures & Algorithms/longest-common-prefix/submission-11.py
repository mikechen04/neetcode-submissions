class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for c in range(len(strs[0])):
            char = strs[0][c]
            for i in range(1, len(strs)):
                if c >= len(strs[i]):
                    return res
                elif strs[i][c] != char:
                    return res

            res += char
        
        return res

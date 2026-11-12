class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        current = ""
        count = 0

        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs) - 1):
            current = strs[i][count]

            if strs[i+1][count] != current:
                return res
            else:
                count += 1
                res += current
                current = ""
    
        return res
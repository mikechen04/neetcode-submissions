class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # have res be the first char of the first str by default
        # iterate through the array
        # if string in strs doesnt start with res:
        # return res, else continue
        res = ""
        for i in range(len(min(strs))-1):
            res = strs[0][:i+1]
            for string in strs:
                if string.startswith(res) == False:
                    return res[:i]
        return res

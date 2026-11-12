class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # have res be the first char of the first str by default
        # iterate through the array
        # if string in strs doesnt start with res:
        # return res, else continue
        sorted(strs)

        if not strs or not strs[0]:
            res = ""
        else:
            res = strs[0][0]
            
        for i in range(len(strs[0])-1):
            res = strs[0][:i+1]
            for string in strs:
                if string == "":
                    return ""
                elif string.startswith(res) == False:
                    return res[:i]
        return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # initalize res to nothing
        # then iterate through a loop
        # add the first letter of the first element onto res
        # then check every str to see if res exists in every str
        # if not, return the string minus the last char

        for i in range(len(strs)-1):
            res += strs[0][i]
            for j in range(i+1, len(strs)):
                if res != strs[j][:i+1]:
                    if len(res) == 1:
                        return ""
                    else:
                        return res[:i]
        
        return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        if len(strs) <= 1:
            return [[strs[0]]]
        
        for string in strs:
            key = tuple(sorted(string))
            if key not in res:
                res[key] = []
            res[key].append(string)
        
        return list(res.values())
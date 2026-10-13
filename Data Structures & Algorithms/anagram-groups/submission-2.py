class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string, put them into the hashmap
        # then, return the elements grouped and with their original lettering

        groups = {}

        if len(strs) <= 1:
            return [strs]
        
        for word in strs:
            tmp = ''.join(sorted(word))
            if tmp in groups:
                groups[tmp].append(word)
            else:
                groups[tmp] = [word]
        
        return list(groups.values())
        
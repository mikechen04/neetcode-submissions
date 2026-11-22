class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        if len(strs) <= 1:
            return [strs]
        
        for word in strs:
            key = ''.join(sorted(word))
            seen[key].append(word)
            
        return list(seen.values())
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_pattern = {}
        map_s = {}

        pattern = list(pattern)
        s = s.split()
        print(s)
        for char in pattern:
            if char in map_pattern:
                map_pattern[char] += 1
            else:
                map_pattern[char] = 1
        
        for char in s:
            if char in map_s:
                map_s[char] += 1
            else:
                map_s[char] = 1
        
        print(map_pattern, map_s)
        return sorted(map_pattern.values()) == sorted(map_s.values())




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort both strings
        # return them equal to each other

        s_sorted = ''.join(sorted(s))
        t_sorted = ''.join(sorted(t))

        return s_sorted == t_sorted
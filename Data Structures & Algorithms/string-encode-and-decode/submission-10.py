class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for char in strs:
            res += char
            res += "<3"
        return res
    def decode(self, s: str) -> List[str]:
        s = s.split("<3")
        s.pop()
        return s
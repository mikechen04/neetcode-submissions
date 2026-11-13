class Solution:

    def encode(self, strs: List[str]) -> str:
        # lets separate words using a unique string of new characters
        # hello, world -> hello<3world
        res = ""
        for char in strs:
            res += char
            res += "<3"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        # split based off of "<3" in the text
        # return
        s = s.split("<3")
        s.pop()
        return s

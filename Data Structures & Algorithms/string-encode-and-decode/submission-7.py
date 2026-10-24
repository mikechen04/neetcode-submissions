class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for char in strs:
            res += char
            res += '❤️'
        return res

    def decode(self, s: str) -> List[str]:
        res_list = s.split("❤️")
        res_list.pop()
        return res_list
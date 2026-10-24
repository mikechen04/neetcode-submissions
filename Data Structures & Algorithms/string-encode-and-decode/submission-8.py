class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for char in strs:
            res += char
            res += '<3'
        return res
    def decode(self, s: str) -> List[str]:
        new_list = s.split('<3')
        new_list.pop()
        return new_list
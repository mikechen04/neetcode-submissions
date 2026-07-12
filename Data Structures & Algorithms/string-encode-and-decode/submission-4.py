class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "encode"
        else:
            return "meow".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "encode":
            return []
        else:
            return s.split("meow")
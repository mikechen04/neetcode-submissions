class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        pairs = {
            "]":"[",
            ")":"(",
            "}":"{"
        }

        while len(s) % 2 == 0:
            if len(s) == 0:
                break
            tmp = s.pop()
            if tmp in pairs:
                s.pop()
        
        return True
            
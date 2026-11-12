class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        s.reverse()

        pairs = {
            "]":"[",
            ")":"(",
            "}":"{"
        }

        while len(s) > 0:
            meow = s.pop()
            if meow == "[" or meow == "(" or meow == "{":
                stack.append(meow)
            else:
                if not stack:
                    return False
                if pairs[meow] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
        if len(s) == 1:
            return False
        else:
            return True
            
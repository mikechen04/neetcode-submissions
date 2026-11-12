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
               if pairs[meow] in stack[-1]:
                stack.pop()

        if len(s) == 1:
            return False
        else:
            return True
            
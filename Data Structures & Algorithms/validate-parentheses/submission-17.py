class Solution:
    def isValid(self, s: str) -> bool:
        # using a stack
        # and implementing a dict with all pairs
        # if brackets are closed in the correct order
        # return true else false

        stack = []
        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        if len(stack) < 1:
            return False

        for i in range(len(s) - 1):
            if s[i] in bracket.keys():
                stack.append(s[i])
            else: # if a closing type
                if stack[-1] == s[-1]: # check for corresponding bracket
                    stack.pop()
                    s.pop()
                else:
                    return False

        return stack
        # return True if len(stack) == 0 else False

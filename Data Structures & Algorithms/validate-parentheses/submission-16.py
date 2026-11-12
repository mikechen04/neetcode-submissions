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

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else: # if a closing type
                if stack[-1] == s[0]: # check for corresponding bracket
                    stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False

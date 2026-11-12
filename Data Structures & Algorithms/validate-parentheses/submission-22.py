class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in range(len(s)):
            if s[i] in brackets:
                stack.append(s[i])
            if stack:
                if stack[-1] in brackets.keys():
                    stack.pop()
            
        return True if len(stack) == 0 else False
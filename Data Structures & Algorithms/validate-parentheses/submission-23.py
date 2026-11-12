class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in range(len(s)):
            if s[i] in brackets.values():
                stack.append(s[i])
            #else:
            #    return False

            if stack:
                if s[i] in brackets.keys():
                    stack.pop()
                #else:
                #    return False
            
        return True if len(stack) == 0 else False
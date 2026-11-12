class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for i in range(len(s)):
            if s[i] in valid.values():
                stack.append(s[i])
            else:
                if len(stack) > 0 and valid[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
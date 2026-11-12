class Solution:
    def isValid(self, s: str) -> bool:
        # base cases
        # if stack length is odd, its automatically false
        if len(s) <= 1:
            return False
        
        stack = []
        valid = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for i in range(len(s)):
            # if s[i] is a value
            if s[i] in valid.values():
                stack.append(s[i])
            # if s[i] is a key
            elif s[i] in valid:
                if len(stack) > 0 and valid[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
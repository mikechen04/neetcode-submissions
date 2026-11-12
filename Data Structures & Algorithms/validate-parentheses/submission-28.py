class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for i in range(len(s)):
            if s[i] in valid.values(): # if its an opening pair
                stack.append(s[i])
            elif s[i] in valid: # if its a closing pair
                if s[i] in valid and valid[s[i]] == stack[-1]: # if the key == value at the top of the stack
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parantheses = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        for char in s:
            if char in parantheses:
                if not stack:
                    return False
                if stack.pop() != parentheses[char]:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = []
        stack = []
        for i in range(len(tokens)):
            # if token index isnumeric, push onto stack
            x = tokens[i]
            # if token index is operand, pop twice off the stack, apply operand, then reapply
            if x == "+":
                meow = stack.pop()
                meow2 = stack.pop()
                arf = meow2 + meow
                stack.append(arf)
            elif x == "-":
                meow = stack.pop()
                meow2 = stack.pop()
                arf = meow2 - meow
                stack.append(arf)
            elif x == "*":
                meow = stack.pop()
                meow2 = stack.pop()
                arf = meow2 * meow
                stack.append(arf)
            elif x == "/":
                meow = stack.pop()
                meow2 = stack.pop()
                arf = meow2 / meow
                stack.append(int(arf))
            else:
                stack.append(int(x))

        # return stack[0] since one value/element is always left
        return int(stack[0])
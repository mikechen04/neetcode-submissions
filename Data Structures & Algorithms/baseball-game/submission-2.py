class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                stack.append(int(num1 + num2))
            elif op == "C":
                stack.pop()
            elif op == "D":
                num = stack[-1]
                stack.append(int(num * 2))
            else:
                stack.append(int(op))
        
        print(stack)
        return sum(stack)

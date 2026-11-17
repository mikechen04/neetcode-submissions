class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        #if len(tokens) == 1:
        #    return int(tokens[0])

        for i in range(len(tokens)):
            if tokens[i] == "+":
                tmp1, tmp2 = int(res.pop()), int(res.pop())
                res.append(tmp2 + tmp1)
            elif tokens[i] == "-":
                tmp1, tmp2 = int(res.pop()), int(res.pop())
                res.append(tmp2 - tmp1)
            elif tokens[i] == "*":
                tmp1, tmp2 = int(res.pop()), int(res.pop())
                res.append(tmp2 * tmp1)
            elif tokens[i] == "/":
                tmp1, tmp2 = int(res.pop()), int(res.pop())
                res.append(tmp2 / tmp1)
            else:
                res.append(int(tokens[i]))
        
        return int(res[0])
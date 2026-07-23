class Solution:
    def calPoints(self, operations: List[str]) -> int:
        operations.reverse()
        res = []
        
        while operations:
            if operations[-1].lstrip('-').isdigit():
                res.append(int(operations[-1]))
                operations.pop()
            elif operations[-1] == "+":
                res.append(res[-1] + res[-2])
                operations.pop()
            elif operations[-1] == "D":
                res.append(res[-1] * 2)
                operations.pop()
            elif operations[-1] == "C":
                res.pop()
                operations.pop()
        
        return sum(res)
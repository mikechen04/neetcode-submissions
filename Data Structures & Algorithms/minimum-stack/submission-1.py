class MinStack:

    def __init__(self):
        self.minstack = []

    def push(self, val: int) -> None:
        self.minstack.append(val)

    def pop(self) -> None:
        self.minstack.pop()

    def top(self) -> int:
        if len(self.minstack) >= 1:
            return self.minstack[-1]
        else:
            return None

    def getMin(self) -> int:
        min = sorted(self.minstack)
        return min[0]

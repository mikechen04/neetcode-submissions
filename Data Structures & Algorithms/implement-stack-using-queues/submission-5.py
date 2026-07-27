class MyStack:

    def __init__(self):
        # initialize stack by using an array
        self.stack = []

    def push(self, x: int) -> None:
        # append x
        self.stack.append(x)

    def pop(self) -> int:
        # use built in function to pop
        return self.stack.pop()

    def top(self) -> int:
        # return self.pop()
        return self.stack[-1]

    def empty(self) -> bool:
        # if len stack > 0 return false else true
        if len(self.stack) > 0:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class MyQueue:

    def __init__(self): # done
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None: # done
        self.stack_in.append(x)

    def pop(self) -> int:
        if len(self.stack_out) == 0:
            while self.stack_in:
                x = self.stack_in.pop()
                self.stack_out.append(x)
        return self.stack_out.pop()

    def peek(self) -> int:
        if len(self.stack_out) == 0:
            while self.stack_in:
                x = self.stack_in.pop()
                self.stack_out.append(x)
        return self.stack_out[-1]

    def empty(self) -> bool:
        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
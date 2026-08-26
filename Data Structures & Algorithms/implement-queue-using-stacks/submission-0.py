class MyQueue:

    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def push(self, x: int) -> None:
        self.stack_a.append(x)

    def pop(self) -> int:
        if not self.stack_b:
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()

    def peek(self) -> int:
        if not self.stack_b:
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b[-1]

    def empty(self) -> bool:
        return not max(len(self.stack_a), len(self.stack_b))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
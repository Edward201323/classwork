class MyQueue:

    def __init__(self):
        self.s = []
        self.q = []

    def push(self, x: int) -> None:
        self.s.append(x)

        self.q.clear()
        s_copy = self.s.copy()
        while s_copy:
            self.q.append(s_copy.pop())


    def pop(self) -> int:
        removed = self.q.pop()

        self.s.clear()
        q_copy = self.q.copy()
        while q_copy:
            self.s.append(q_copy.pop())
        
        return removed

    def peek(self) -> int:
        if self.q:
            return self.q[len(self.q) - 1]
        else:
            return -1

    def empty(self) -> bool:
        if self.q:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.q_sum = 0

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.q_sum -= self.q.popleft()
            
        self.q.append(val)
        self.q_sum += val
        
        return self.q_sum / len(self.q)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class MovingAverage:

    def __init__(self, size: int):
        self.list = []
        self.size = size
        self.num = 0

    def next(self, val: int) -> float:
        if self.num < self.size:
            self.list.append(val)
        else:
            self.list[self.num % self.size] = val

        self.num += 1

        return sum(self.list) / len(self.list)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

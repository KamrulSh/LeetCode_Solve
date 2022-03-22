class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.count = 0
        
    def push(self, x: int) -> None:
        if self.maxSize > self.count:
            self.count += 1
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            self.count -= 1
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        inc = min(k, len(self.stack))
        for idx in range(inc):
            self.stack[idx] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
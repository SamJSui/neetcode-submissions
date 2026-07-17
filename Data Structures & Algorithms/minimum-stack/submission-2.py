class MinStack:

    def __init__(self):
        self.stk = deque()
        self.mini = deque()

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.mini or val < self.mini[-1]:
            self.mini.append(val) 
        else:
            self.mini.append(self.mini[-1])
    
    def pop(self) -> None:
        self.stk.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mini[-1]

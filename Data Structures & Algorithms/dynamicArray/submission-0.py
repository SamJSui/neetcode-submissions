class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.last = 0
        self.arr = [0]*capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.last == self.cap:
            self.resize()
        self.arr[self.last] = n
        self.last += 1

    def popback(self) -> int:
        self.last -= 1
        return self.arr[self.last]

    def resize(self) -> None:
        self.cap *= 2
        self.arr = self.arr + [0] * (self.getCapacity() - self.getSize())

    def getSize(self) -> int:
        return self.last
    
    def getCapacity(self) -> int:
        return self.cap

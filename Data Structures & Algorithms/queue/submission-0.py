class Node:
    def __init__(self, val=-1, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# With insertTail, I'm just making a DLL
class LinkedList:
    
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.tail.prev, self.head.next = self.head, self.tail
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length: 
            return -1

        if index <= self.length // 2:
            tmp = self.head.next
            for _ in range(index):
                tmp = tmp.next
            return tmp.val
        else:
            tmp = self.tail.prev
            for _ in range(self.length-index-1):
                tmp = tmp.prev
            return tmp.val

class Deque:
    
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.tail.prev, self.head.next = self.head, self.tail
        self.length = 0

    def isEmpty(self) -> bool:
        return self.length == 0

    def append(self, value: int) -> None:
        prev = self.tail.prev
        node = Node(value, self.tail, prev)
        self.tail.prev = node
        prev.next = node
        self.length += 1

    def appendleft(self, value: int) -> None:
        nxt = self.head.next
        node = Node(value, nxt, self.head)
        self.head.next = node
        nxt.prev = node
        self.length += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last = self.tail.prev
        self._delete(last)
        return last.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first = self.head.next
        self._delete(first)
        return first.val

    def _delete(self, node: Node):
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev
        self.length -= 1

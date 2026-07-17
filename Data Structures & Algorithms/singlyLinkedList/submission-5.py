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

    def insertHead(self, val: int) -> None:
        nxt = self.head.next
        node = Node(val, nxt, self.head)
        self.head.next = node
        nxt.prev = node
        self.length += 1

    def insertTail(self, val: int) -> None:
        prev = self.tail.prev
        node = Node(val, self.tail, prev)
        self.tail.prev = node
        prev.next = node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False

        if index <= self.length // 2:
            tmp = self.head.next
            for _ in range(index):
                tmp = tmp.next
            self._delete(tmp)
        else:
            tmp = self.tail.prev
            for _ in range(self.length-index-1):
                tmp = tmp.prev
            self._delete(tmp)
        return True

    def getValues(self) -> List[int]:
        tmp = self.head.next
        vals = []
        while tmp != self.tail:
            vals.append(tmp.val)
            tmp = tmp.next
        return vals

    def _delete(self, node: Node):
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev
        self.length -= 1

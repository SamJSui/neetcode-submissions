class LRUCache:

    def __init__(self, capacity: int):
        self.q = deque()
        self.cap = capacity
        self.d = {}

    def get(self, key: int) -> int:
        print(f'get key: {key}')
        if key not in self.d: 
            print('got -1\n')
            return -1
        n = len(self.q)
        for _ in range(n):
            top = self.q.popleft()
            if top != key: self.q.append(top)
        self.q.append(key)
        print(f'got {self.d[key]}')
        print(f'd {self.d}')
        print(f'q {self.q}\n')
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        print(f'put key: {key} val: {value}')
        if key in self.d:
            n = len(self.q)
            for _ in range(n):
                top = self.q.popleft()
                if top != key: self.q.append(top)
        self.q.append(key)
        self.d[key] = value
        
        if len(self.q) > self.cap:
            top = self.q.popleft()
            del self.d[top]
        print(f'd: {self.d}')
        print(f'q: {self.q}\n')

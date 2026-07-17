class UnionFind:
    
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.par[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        else:
            self.par[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        self.components -= 1
        return True


    def getNumComponents(self) -> int:
        return self.components

class Dsu:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
        self.comps = n
    
    def find(self, i: int) -> int:
        ''' Find parent of node i
        '''

        if self.par[i] != i:
            self.par[i] = self.find(self.par[i])
        return self.par[i]

    def union(self, i: int, j: int) -> bool:
        root_i, root_j = self.find(i), self.find(j)
        if root_i == root_j:
            return False
        if self.rank[root_i] < self.rank[root_j]:
            self.par[root_i] = root_j
        elif self.rank[root_j] < self.rank[root_i]:
            self.par[root_j] = root_i
        else:
            self.par[root_i] = root_j
            self.rank[root_j] += 1
        self.comps -= 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = Dsu(n)
        for src, sink in edges:
            dsu.union(src, sink)
        return dsu.comps
        
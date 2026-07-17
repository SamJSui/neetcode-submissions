class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bananas = 0
        q = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    bananas += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        for row in grid:
            print(row)
        time = 0
        visited = set()
        while q and bananas:
            size = len(q)
            print(q)
            for _ in range(size):
                i, j = q.popleft()
                if (i, j) in visited: continue
                visited.add((i, j))

                for i1, j1 in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if i1 < 0 or i1 >= m: continue
                    if j1 < 0 or j1 >= n: continue
                    if (i1, j1) in q or (i1, j1) in visited or grid[i1][j1] != 1: continue
                    q.append((i1, j1))
                    bananas -= 1
            time += 1
        return time if bananas == 0 else -1
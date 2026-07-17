class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        def dfs(i, j):
            if (i, j) in visited: return 0
            if i < 0 or j < 0: return 0
            if i >= m or j >= n: return 0
            if grid[i][j] == 0: return 0
            visited.add((i, j))
            
            up, down = dfs(i-1, j), dfs(i+1, j)
            left, right = dfs(i, j-1), dfs(i, j+1)
            return 1+up+down+left+right            

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ret = max(ret, dfs(i, j))
        return ret
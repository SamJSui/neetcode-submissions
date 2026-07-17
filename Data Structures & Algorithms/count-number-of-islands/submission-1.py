class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != "0" and (r, c) not in visited:
                    self._dfs(r, c, grid, visited)
                    islands += 1
        return islands

    def _dfs(self, r: int, c: int, grid: List[List[str]], visited: set):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        if (r, c) in visited:
            return
        if grid[r][c] == "0":
            return
        visited.add((r, c))
        self._dfs(r+1, c, grid, visited)
        self._dfs(r-1, c, grid, visited)
        self._dfs(r, c+1, grid, visited)
        self._dfs(r, c-1, grid, visited)
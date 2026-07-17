class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        fresh, rotten_cnt = 0, 0
        rotten = deque()
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        time = 0
        while fresh > 0 and rotten:
            print(rotten)
            size = len(rotten)
            for z in range(size):
                top = rotten.popleft()

                for di, dj in [(top[0]-1, top[1]), (top[0]+1, top[1]), (top[0], top[1]-1), (top[0], top[1]+1)]:
                    if di >= 0 and dj >= 0 and di < m and dj < n and grid[di][dj] == 1 and (di, dj) not in visited:
                        visited.add((di, dj))
                        rotten.append((di, dj))
                        fresh -= 1
            time += 1

        return time if fresh == rotten_cnt else -1
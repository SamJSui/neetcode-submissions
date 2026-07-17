class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r: int, c: int, i: int) -> bool:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if (r, c) in visited:
                return False
            print(board[r][c], word[i])

            visited.add((r, c))
            if word[i] != board[r][c]:
                visited.remove((r, c))
                return False
            if i == len(word)-1:
                return True
            check = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            visited.remove((r, c))
            return check

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
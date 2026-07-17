class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        squares = [[False] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': 
                    continue
                sq_index = (i // 3) * 3 + (j//3)
                val = int(board[i][j])-1
                if rows[i][val]:
                    return False
                else:
                    rows[i][val] = True

                if cols[j][val]:
                    return False
                else:
                    cols[j][val] = True

                if squares[sq_index][val]:
                    return False
                else:
                    squares[sq_index][val] = True

        return True
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix)-1, len(matrix[0])-1
        i = 0
        for row in matrix:
            print(row)
        while i <= m:
            row_mid = (i+m)//2
            j = 0
            r = n
            while j <= r:
                col_mid = (j+r)//2
                print(f'mid: {matrix[row_mid][col_mid]}')
                if matrix[row_mid][col_mid] == target:
                    return True
                elif matrix[row_mid][col_mid] > target:
                    r = col_mid-1
                else:
                    j = col_mid+1
            
            print(f'matrix[i][0]: {matrix[i][0]} matrix[m][0]: {matrix[m][0]}')
            # if matrix[i][0] == target or matrix[m][0] == target:
            #     return True
            if target > matrix[row_mid][0]:
                i = row_mid+1
            else:
                m = row_mid-1
        
        return False
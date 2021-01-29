class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix),len(matrix[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==1:
                    if i==0 or j == 0:
                        count += 1
                    else:
                        matrix[i][j] = min(matrix[i][j-1],matrix[i-1][j-1],matrix[i-1][j]) + 1
                        count += matrix[i][j]
        return count
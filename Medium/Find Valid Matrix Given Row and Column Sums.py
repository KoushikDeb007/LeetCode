class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row, col = len(rowSum), len(colSum)
        mat = [[0 for i in range(col)] for i in range(row)]
        # print(mat)
        for i in range(row):
            for j in range(col):
                # print(rowSum[i],colSum[j])
                mat[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= mat[i][j]
                colSum[j] -= mat[i][j]
        return mat


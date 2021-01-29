###### video explanation
# https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        RC, CC = len(mat), len(mat[0])
        for row in range(RC):
            for col in range(1, CC):
                mat[row][col] += mat[row][col - 1]
        for col in range(CC):
            for row in range(1, RC):
                mat[row][col] += mat[row - 1][col]
        result = []

        for row in range(RC):
            res = []
            for col in range(CC):
                A, D, B, C = max(row - K, 0), min(row + K, RC - 1), max(col - K, 0), min(col + K, CC - 1)
                val = mat[D][C]
                if A - 1 < 0 or B - 1 < 0:
                    val += 0
                else:
                    val += mat[A - 1][B - 1]
                if A - 1 >= 0:
                    val -= mat[A - 1][C]
                if B - 1 >= 0:
                    val -= mat[D][B - 1]
                res.append(val)
            result.append(res)
        return result
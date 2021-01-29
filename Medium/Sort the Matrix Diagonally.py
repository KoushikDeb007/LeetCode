import collections


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[i - j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse=1)
        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i - j].pop()
        return mat
#         row,col = len(mat),len(mat[0])

#         for c in range(col):
#             i,j = 0,c
#             temp = []
#             while(i<row and j<col):
#                 temp.append(mat[i][j])
#                 i+=1
#                 j+=1
#             temp.sort()
#             i,j = 0,c
#             for t in temp:
#                 mat[i][j] = t
#                 i+=1
#                 j+=1
#         for r in range(1,row):
#             i,j = r,0
#             temp = []
#             while(i<row and j<col):
#                 temp.append(mat[i][j])
#                 i+=1
#                 j+=1
#             temp.sort()
#             i,j = r,0
#             for t in temp:
#                 mat[i][j] = t
#                 i+=1
#                 j+=1
#         return mat


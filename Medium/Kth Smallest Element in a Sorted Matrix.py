class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        for i in range(min(k, len(matrix))):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        numbercount = number = 0
        while (len(heap)):
            number, row, col = heapq.heappop(heap)
            numbercount += 1
            if numbercount == k:
                return number
            if len(matrix[row]) > col + 1:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        return number

        # num = []
        # for i in matrix:
        #     num.extend(i)
        # num.sort()
        # return num[k-1]
#         n = len(matrix)
#         start, end = matrix[0][0], matrix[n - 1][n - 1]
#         while start < end:
#             mid = start + (end - start) / 2
#             smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

#             count, smaller, larger = self.count_less_equal(matrix, mid, smaller, larger)

#             if count == k:
#                 return smaller
#             if count < k:
#                 start = larger  # search higher
#             else:
#                 end = smaller  # search lower

#         return start


#     def count_less_equal(self,matrix, mid, smaller, larger):
#         count, n = 0, len(matrix)
#         row, col = n - 1, 0
#         while row >= 0 and col < n:
#             if matrix[row][col] > mid:
#               # as matrix[row][col] is bigger than the mid, let's keep track of the
#               # smallest number greater than the mid
#                 larger = min(larger, matrix[row][col])
#                 row -= 1
#             else:
#               # as matrix[row][col] is less than or equal to the mid, let's keep track of the
#               # biggest number less than or equal to the mid
#                 smaller = max(smaller, matrix[row][col])
#                 count += row + 1
#                 col += 1

#         return count, smaller, larger

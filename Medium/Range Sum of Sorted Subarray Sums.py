# class Solution(object):
#     def rangeSum(self, nums, n, left, right):
#         """
#         :type nums: List[int]
#         :type n: int
#         :type left: int
#         :type right: int
#         :rtype: int
#         """
#         res = []
#         for i in range(n):
#             res.append(nums[i])
#             for j in range(i+1,n):
#                 res.append(res[-1]+nums[j])

#         res.sort()
#         result = 0
#         for i in range(left-1,right):
#             result+=res[i]
#         return result%1000000007
import heapq


class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        h = []
        for i in range(n):
            heapq.heappush(h, (nums[i], i))
        # print heappop(h)
        result = 0
        count = 1
        while count <= right:
            q = heapq.heappop(h)
            if count >= left:
                result = (result + q[0]) % (10 ** 9 + 7)
            count += 1
            if q[1] < n - 1:
                heapq.heappush(h, (nums[q[1] + 1] + q[0], q[1] + 1))
        return result

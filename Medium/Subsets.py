class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(ind, n, path):
            # print(res)
            res.append(path)
            for i in range(ind, n, 1):
                dfs(i + 1, n, path + [nums[i]])

        res = []
        dfs(0, len(nums), [])
        return res


# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         nums.sort()
#         self.dfs(nums, 0, [], res, len(nums))
#         return res
#
#     def dfs(self, nums, index, path, res, nlen):
#         res.append(path)
#         for i in range(index, nlen, 1):
#             self.dfs(nums, i + 1, path + [nums[i]], res, nlen)

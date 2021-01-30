class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(nlen, nums, path):
            if not nums:
                res.append(path)
            for i in range(nlen):
                permutations(nlen - 1, nums[:i] + nums[i + 1:], path + [nums[i]])

        res = []
        nlen = len(nums)
        permutations(nlen, nums, [])
        return res


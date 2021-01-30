class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #         s = set()
        #         res = []
        #         for i in nums:
        #             if i in s:
        #                 res.append(i)
        #             else:
        #                 s.add(i)
        #         return res
        res = []

        for x in nums:
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return res

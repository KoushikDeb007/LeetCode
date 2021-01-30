class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        for i in nums:
            res ^= i

        i = 0
        while (True):
            if res & (1 << i):
                break
            else:
                i += 1
            if i > 31:
                break
        one = 0
        two = 0
        for n in nums:
            if n & (1 << i):
                one ^= n
            else:
                two ^= n
        return [one, two]
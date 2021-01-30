from collections import Counter


class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        alen = len(arr)
        if alen <= k:
            return 0
        v = Counter(arr)
        val = sorted(v.values())
        for i, c in enumerate(val):
            if k >= c:
                k -= c
            else:
                return len(val) - i

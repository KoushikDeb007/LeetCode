class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c = Counter(arr)
        alen = len(arr)
        res = 0
        count = 0
        for item in c.most_common():
            count += item[1]
            res += 1
            if count >= alen // 2:
                return res
        # return 2

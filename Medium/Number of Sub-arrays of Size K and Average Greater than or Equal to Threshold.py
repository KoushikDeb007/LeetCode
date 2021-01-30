class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res = 0
        alen = len(arr)
        summ = sum(arr[:k])
        if summ // k >= threshold:
            res += 1
        for j in range(k, alen):

            summ = summ + arr[j] - arr[j - k]
            if summ // k >= threshold:
                res += 1

        return res

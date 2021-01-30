class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        res = [1, 1]
        a, b = 1, 1
        while (a <= k):
            res.append(a + b)
            b = a
            a = res[-1]
        c = 1
        while res[-1] > k:
            res.pop()
        val = res[-1]
        i = len(res) - 2
        while (val != k):
            if val + res[i] == k:
                c += 1
                return c
            elif val + res[i] < k:
                c += 1
                val += res[i]
                i -= 1
            else:
                i -= 1
        return c

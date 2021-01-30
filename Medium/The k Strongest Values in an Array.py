class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        #         arr.sort()
        #         nlen = len(arr)
        #         median = arr[(nlen-1)//2]
        #         h = []
        #         for i in arr:
        #             heappush(h,(-abs(i-median),-i))

        #         res = []
        #         for i in range(k):
        #             res.append(-1*heappop(h)[1])
        #         return res
        if not arr or not k:
            return []

        if len(arr) <= k:
            return arr

        arr = sorted(arr)
        n = len(arr)
        median = arr[(n - 1) // 2]

        res = []
        l = 0
        r = n - 1
        while l < r and len(res) < k:
            if median - arr[l] > arr[r] - median:
                res.append(arr[l])
                l += 1
            else:
                res.append(arr[r])
                r -= 1

        return res

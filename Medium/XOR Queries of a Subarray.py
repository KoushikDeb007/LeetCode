class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        alen = len(arr)
        for i in range(1, alen):
            arr[i] = arr[i] ^ arr[i - 1]
        res = []
        for q in queries:
            if q[0] == 0:
                res.append(arr[q[1]])
            else:
                res.append(arr[q[1]] ^ arr[q[0] - 1])
        return res

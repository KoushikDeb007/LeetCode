class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        :type arr: List[int]
        :rtype: int
        """

        ##Brute forece##
        # total,nlen = 0,len(arr)
        # for i in range(nlen-1):
        #     xor = arr[i]
        #     for j in range(i+1,nlen):
        #         if xor == arr[j]:
        #             length = j - i
        #             total += length
        #         xor ^= arr[j]
        # return total
        prefix = {0: [-1, 1]}
        res, cur = 0, 0
        for i, v in enumerate(arr):
            cur ^= v
            idxSum, cnt = prefix.get(cur, [0, 0])
            # print(prefix,cur,idxSum,cnt)
            res += i * cnt - idxSum - cnt
            prefix[cur] = [idxSum + i, cnt + 1]
        return res

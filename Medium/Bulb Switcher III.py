class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        # N = max(light)
        # res = [-1]*N
        # i = 0
        # maxp = -1
        # count = 0
        # for l in light:
        #     if l>maxp:
        #         maxp = l
        #     res[l-1] = 1
        #     while(i<N and res[i]==1):
        #         i+=1
        #     if i == maxp:
        #         count += 1
        # return count
        res = 0
        bulb_sum = 0
        idx_sum = 0

        for i in range(len(light)):
            bulb_sum += light[i]
            idx_sum += i + 1
            if idx_sum == bulb_sum:
                res += 1
        return res
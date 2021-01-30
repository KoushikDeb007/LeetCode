class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #         f = [0]*33
        #         for a in nums:
        #             aa = bin(a)
        #             if aa[0]=='-':
        #                 f[0]+=1
        #                 aa = aa[3:]
        #             else:
        #                 aa = aa[2:]
        #             aa = aa.rjust(33,'0')

        #             for i in range(33):
        #                 if aa[i]=='1':
        #                     f[i]+=1
        #         res = []
        #         for i in f[1:]:
        #             if i%3==1:
        #                 res.append('1')
        #             else:
        #                 res.append('0')
        #         val = int(''.join(res),2)
        #         if f[0]%3==1:
        #             return -val
        #         return val
        #         ans = 3 * sum(set(nums))
        #         ans -= sum(nums)
        #         ans /= 2
        #         return(ans)

        single_num = 0

        for bit_shift in range(32):
            sum1 = 0

            for number in nums:
                sum1 += (number >> bit_shift) & 1
            single_num |= (sum1 % 3) << bit_shift

        if (single_num & (1 << 31)) == 0:
            return single_num
        else:
            return -((single_num ^ (0xFFFF_FFFF)) + 1)
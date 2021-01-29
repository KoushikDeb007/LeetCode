class Solution:
    def minFlips(self, target: str) -> int:
        return 2 * target.count('10') + (target[-1] == '1')
        # count = 0
        # for i in target:
        #     if count%2==0:
        #         if i=='1':
        #             count += 1
        #     else:
        #         if i=='0':
        #             count += 1
        # return count
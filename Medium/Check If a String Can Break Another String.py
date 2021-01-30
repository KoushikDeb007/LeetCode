# class Solution:
#     def checkIfCanBreak(self, s1: str, s2: str) -> bool:
# l1 = [char for char in s1]
# l1.sort()
# l2 = [char for char in s2]
# l2.sort()
# strlen = len(s1)
# flag = 0
# for i in range(strlen):
#     if l1[i]>=l2[i]:
#         continue
#     else:
#         flag = 1
#         break
# if flag:
#     for i in range(strlen):
#         if l1[i]<=l2[i]:
#             continue
#         else:
#             return False
# return True
import collections


class Solution:
    def check(self, d1, d2):
        # print(d1,d2)
        s = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            s += d1[c] - d2[c]
            # print(s,d1[c],d2[c])
            if s < 0:
                return False
        return True

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        d1 = collections.Counter(s1)
        d2 = collections.Counter(s2)
        return self.check(d1, d2) | self.check(d2, d1)
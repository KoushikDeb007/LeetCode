class Solution:
    def minSteps(self, s: str, t: str) -> int:
#         d = {}
#         for i in s:
#             if i in d:
#                 d[i]+=1
#             else:
#                 d[i]=1
#         cnt = 0
#         for i in t:
#             if i in d and d[i]>0:
#                 d[i]-=1
#             else:
#                 cnt+=1
#         return cnt
        abc = 'abcdefghijklmnopqrstuvwxyz'
        return int(sum(abs(t.count(l)-s.count(l)) for l in abc)/2)
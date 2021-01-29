# class Solution:
#     def partitionLabels(self, S: str) -> List[int]:
#         d = {}
#         for i in range(len(S)):
#             if S[i] in d:
#                 d[S[i]][1]= i
#             else:
#                 d[S[i]]=[i,i]
#         i = 0
#         res = []
#         # print(d)
#         while(i<len(S)):
#             end = d[S[i]][1]
#             j = i+1
#             while (j<end):
#                 # print(S[j],d[S[j]][1],end)
#                 if d[S[j]][1]>end:
#                     end = d[S[j]][1]
#                 j+=1

#             res.append(end-i+1)
#             i = end+1
#         return res
from collections import defaultdict


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        d = defaultdict(list)
        slen = len(S)
        for i in range(slen):
            d[S[i]].append(i)
        start, end = d[S[0]][0], d[S[0]][-1]
        ls = []
        while (end < slen):
            i = start + 1
            while (i < end):
                # for i in range(start+1,end):
                if d[S[i]][-1] > end:
                    end = d[S[i]][-1]
                i += 1
            ls.append(end - start + 1)
            # print(ls)
            start = end + 1
            if start >= slen:
                break
            # print(start)
            end = d[S[start]][-1]
        return ls
        #     last = {c: i for i,c in enumerate(S)}
        # anchor = j = 0
        # ans = []
        # for i,c in enumerate(S):
        #     j = max(j,last[c])
        #     #print("I",i,"C",c,"J",j)
        #     if i==j:
        #         #print("i-anchor + 1",i-anchor + 1)
        #         ans.append(i-anchor + 1)
        #         anchor = i+1
        # return ans
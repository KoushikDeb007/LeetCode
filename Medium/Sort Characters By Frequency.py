class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = collections.Counter(s)

        # Build string
        res = []
        for k, v in cnt.most_common():
            res += [k] * v
        return "".join(res)
        # d = {}
        # for i in s:
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i] = 1
        # d = sorted(d.items(),key= lambda item:item[1],reverse= True)
        # # print(d)
        # l = []
        # for i in d:
        #     l.append(i[0]*i[1])
        # return "".join(l)
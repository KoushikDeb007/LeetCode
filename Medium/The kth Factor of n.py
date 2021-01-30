class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                res.append(i)
                if i!=n//i:
                    res.append(n//i)
        # print(res)
        if len(res)>=k:
            res.sort()
            return res[k-1]
        return -1
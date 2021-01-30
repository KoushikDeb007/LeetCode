class DSU:
    def __init__(self, N):
        self.p = list(range(N + 1))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp:
            return -1
        else:
            self.p[xp] = yp
            return 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges) + 1)
        ret = None

        for x, y in edges:
            val = dsu.union(x, y)
            if val == -1:
                ret = [x, y]
        return ret

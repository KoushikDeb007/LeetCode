class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp:
            return 1
        self.p[xp] = yp
        return 0


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        dsu = DSU(n)
        result = 0
        for x, y in connections:
            dsu.union(x, y)
        for i in range(len(dsu.p)):
            if i != dsu.p[i]:
                result += 1
        # print(result)
        return n - result - 1


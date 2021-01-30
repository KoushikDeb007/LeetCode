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
            return
        self.p[xp] = yp


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        seen = set()

        def dfs(node):
            for nei, adj in enumerate(M[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans
        # dsu = DSU(len(M))
        # for i in range(len(M)):
        #     for j in range(len(M[i])):
        #         if M[i][j]==1:
        #             dsu.union(i,j)
        # return len({dsu.find(i) for i in range(len(M))})
#         friends = [i for i in range(len(M))]
#         queue = []
#         circles = 0
#         while friends:
#             # print(friends)
#             circles+=1
#             f = friends[0]
#             queue.append(M[f])
#             while queue:
#                 # print(queue)
#                 q = queue.pop()
#                 for i,r in enumerate(q):
#                     if r == 1 and i in friends:
#                             friends.remove(i)
#                             if f!=i :
#                                 queue.append(M[i])
#         return circles


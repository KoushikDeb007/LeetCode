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
        print('first', self.p)
        print(x, xp, self.p[xp], y, yp)
        self.p[xp] = yp
        print('second', self.p)


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        dsu = DSU(20000)

        for x, y in stones:
            # print(x,y)
            dsu.union(x, y + 10000)
        print(dsu.p)
        print([dsu.find(x) for x, y in stones])
        return N - len({dsu.find(x) for x, y in stones})

#         graph,moves = defaultdict(list),0
#         visited = [0]*len(stones)

#         def dfs(node,val=0):
#             visited[node] = 1
#             for child in graph[node]:
#                 if not visited[child]:
#                     val =1 + dfs(child,val)
#             return val

#         for i in range(len(stones)):
#             for j in range(i):
#                 if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
#                     graph[i].append(j)
#                     graph[j].append(i)

#         for node in range(len(stones)):
#             if not visited[node]:
#                 moves+=dfs(node)
#         return moves

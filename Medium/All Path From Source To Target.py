class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #         n = len(graph)
        #         visited = [0]*n
        #         res = []
        #         self.dfs(0,n-1,graph,res,visited,[0])
        #         return res

        #     def dfs(self,start,end,graph,res,visited,path):
        #         if visited[start]==0:
        #             if start == end:
        #                 res.append(path)
        #                 return
        #             visited[start]=1
        #             for child in graph[start]:
        #                 if visited[child]==0:
        #                     self.dfs(child,end,graph,res,visited,path+[child])
        #                     visited[child]=0

        def dfs(start, end, path, res):
            if start == end:
                res.append(path)
                return
            for child in graph[start]:
                dfs(child, end, path + [child], res)

        n = len(graph)
        # visited = [0]*n
        res = []
        dfs(0, n - 1, [0], res)
        return res


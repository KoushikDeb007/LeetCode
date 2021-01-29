import itertools
import math
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        #         result = set()
        #         vis = [0]*len(tiles)

        #         def dfs(res,depth):
        #             if res:
        #                 result.add(res)
        #             # if depth == len(tiles)-1:
        #             #     result.add(res)

        #             for i in range(len(tiles)):
        #                 if not vis[i]:
        #                     vis[i] = 1
        #                     dfs(res+tiles[i],depth+1)
        #                     vis[i] = 0

        #         dfs('',-1)
        #         return len(result)
        res = 0
        print(Counter(tiles).values())
        freqs = [f + 1 for f in Counter(tiles).values()]
        print(freqs)
        for t in itertools.product(*map(range, freqs)):
            print(t, sum(t), math.factorial(sum(t)))
            n = sum(t)
            subtotal = math.factorial(n)
            for freq in t:
                subtotal //= math.factorial(freq)
            res += subtotal
        return res - 1
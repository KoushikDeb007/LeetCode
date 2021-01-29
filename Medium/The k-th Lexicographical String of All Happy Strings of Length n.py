# class Solution:
#     def getHappyString(self, n: int, k: int) -> str:

#         def dfs(ind,nlen,path,res):
#             if ind == nlen:
#                 res.append(path)
#                 return
#             for i in range(3):
#                 if len(path)==0 or (path[-1]!=ls[i]):
#                     dfs(ind+1,nlen,path+ls[i],res)

#         ls = ['a','b','c']
#         vis = [0]*3
#         res = []
#         dfs(0,n,'',res)
#         res.sort()
#         if len(res)<k:
#             return ''
#         return res[k-1]

# class Solution:
#     def getHappyString(self, n: int, k: int) -> str:
#         k -= 1
#         if k // 2 ** (n - 1) > 2: return ''
#         result, lookup = '^', {'^': 'abc', 'a': 'bc', 'b': 'ac', 'c': 'ab'}
#         for i in reversed(range(n)):
#             idx, k = divmod(k, 2 ** i)
#             result += lookup[result[-1]][idx]
#         return result[1:]
from math import ceil


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        single_ele = 2 ** (n - 1)
        if k > 3 * single_ele:
            return ""
        result = ['a', 'b', 'c'][ceil(k / single_ele) - 1]
        while single_ele > 1:
            k = (k - 1) % single_ele + 1
            single_ele = single_ele // 2
            if result[-1] == 'a':
                result += ['b', 'c'][ceil(k / single_ele) - 1]
            elif result[-1] == 'b':
                result += ['a', 'c'][ceil(k / single_ele) - 1]
            else:
                result += ['a', 'b'][ceil(k / single_ele) - 1]
        return result
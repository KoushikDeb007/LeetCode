class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        #         def dfs(ind,slen,path,res):
        #             if len(path)==slen:
        #                 res.append(path)

        #             for i in range(ind,slen,1):
        #                 dfs(i+1,slen,path+S[i],res)
        #                 if 'a'<=S[i]<='z':
        #                     dfs(i+1,slen,path+S[i].upper(),res)

        #         res = []
        #         S = S.lower()
        #         slen = len(S)
        #         dfs(0,slen,'',res)
        #         return res
        L = [set([char.lower(), char.upper()]) for char in S]
        print(L)
        return map(''.join, product(*L))
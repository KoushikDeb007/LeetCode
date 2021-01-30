class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            res.extend([i + 1, x])
            arr = arr[:i:-1] + arr[:i]
        return res
        #         count, alen = 0, len(arr)
        #         sortedarr = sorted(arr)
        #         res = []
        #         if sortedarr==arr:
        #             return res
        #         # print(sortedarr,arr)
        #         end = alen-1
        #         while(count<alen):
        #             maxval,maxind = -99,0
        #             for ind, val in enumerate(arr[:end+1]):
        #                 if val>maxval:
        #                     maxval = val
        #                     maxind = ind
        #             if maxind!=end:
        #                 i,j = 0,maxind
        #                 while(i<j):
        #                     arr[i],arr[j] = arr[j],arr[i]
        #                     i+=1
        #                     j-=1
        #                 res.append(maxind+1)
        #                 i,j = 0,end
        #                 while(i<j):
        #                     arr[i],arr[j] = arr[j],arr[i]
        #                     i+=1
        #                     j-=1
        #                 res.append(end+1)
        #                 if sortedarr==arr:
        #                     break

        #             end-=1
        #         return res
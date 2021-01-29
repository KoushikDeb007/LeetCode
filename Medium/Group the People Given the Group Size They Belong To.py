from collections import defaultdict


class Solution:
    # Time: O(n)
    # Space: O(n)
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        #         res, dic = [], {}
        #         for idx, group in enumerate(groupSizes):
        #             if group not in dic:
        #                 dic[group] = [idx]
        #             else:
        #                 dic[group].append(idx)

        #             if len(dic[group]) == group:
        #                 res.append(dic[group])
        #                 del dic[group]
        #         return res
        res, dic = [], defaultdict(list)
        for i in range(len(groupSizes)):
            dic[groupSizes[i]].append(i)
            if len(dic[groupSizes[i]]) == groupSizes[i]:
                res.append(dic[groupSizes[i]])
                del dic[groupSizes[i]]

        return res

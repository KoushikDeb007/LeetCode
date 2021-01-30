class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combSum(tar, ind, path, clen):
            # print(path)
            if tar == 0:
                res.append(path)
                return
            if tar < 0:
                return
            for i in range(ind, clen, 1):
                combSum(tar - candidates[i], i, path + [candidates[i]], clen)

        res = []
        candidates.sort()
        combSum(target, 0, [], len(candidates))
        return res
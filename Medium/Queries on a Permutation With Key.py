class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1, m + 1))
        r = []
        for i in queries:
            idx = p.index(i)
            r.append(idx)
            del p[idx]
            p.insert(0, i)
        return r

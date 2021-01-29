class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        res = 0
        j = len(piles) - 1
        for i in range(1, len(piles), 2):
            if i >= j:
                return res
            res += piles[i]
            j -= 1
        return res

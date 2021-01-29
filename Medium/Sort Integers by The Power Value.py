class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        temp = []
        for i in range(lo, hi + 1):
            cnt = 0
            j = i
            while (j != 1):
                if j % 2 == 0:
                    j /= 2

                else:
                    j = 3 * j + 1

                cnt += 1
            temp.append((i, cnt))
        temp.sort(key=lambda a: a[1])

        return temp[k - 1][0]
from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums  # store nums

    def pick(self, target: int) -> int:

        ans = None
        cnt = 0
        for i, x in enumerate(self.nums):
            if x == target:
                cnt += 1
                ok = randint(1, cnt)
                # print(cnt,i,ok)

                if ok == cnt: ans = i  # prob 1/cnt
        return ans
from collections import Counter


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        # res = ''
        # for ch in S:
        #     res+=ch*T.count(ch)
        # for ch in T:
        #     if ch not in S:
        #         res+=ch
        # return res
        ct = Counter(T)
        cs = Counter(S)

        ans = []

        for char in S:
            ans.extend([char] * ct[char])

        for i in range(26):
            char = chr(ord('a') + i)
            if char not in cs:
                ans.extend([char] * ct[char])

        return "".join(ans)
class Solution:
    def numSplits(self, s: str) -> int:
        slen = len(s)
        count = 0
        set1, set2 = {}, {}
        if len(s) == 0:
            return 0
        set1[s[0]] = 1
        for i in range(1, slen):
            if s[i] in set2:
                set2[s[i]] += 1
            else:
                set2[s[i]] = 1
        s1 = len(set1.keys())
        s2 = len(set2.keys())
        if s1 == s2:
            count += 1
        for i in range(1, slen):
            if s[i] in set1:
                set1[s[i]] += 1
            else:
                set1[s[i]] = 1
                s1 += 1
            set2[s[i]] -= 1
            if set2[s[i]] == 0:
                del set2[s[i]]
                s2 -= 1

            if s1 == s2:
                count += 1
        return count
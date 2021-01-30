class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        res = []
        vlen = len(votes[0])
        for i in range(26):
            newv = [0]*vlen
            newv.append(i)
            res.append(newv)
        for vote in votes:
            for i in range(vlen):
                res[ord(vote[i])-65][i]+=1
        res.sort(reverse=True, key=lambda x :tuple(x[i] for i in range(vlen)))
        s = ""
        for i in range(vlen):
            s+=chr(65+res[i][-1])
        return s
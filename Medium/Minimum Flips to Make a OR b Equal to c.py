class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        aa = bin(a)[2:]
        bb = bin(b)[2:]
        cc = bin(c)[2:]
        max_length = max(len(aa),len(bb),len(cc))
        aa = aa.rjust(max_length,'0')
        bb = bb.rjust(max_length,'0')
        cc = cc.rjust(max_length,'0')
        # print(aa,bb,cc)
        count = 0
        for i in range(0,max_length):
            if cc[i]=='1':
                if aa[i]=='0' and bb[i]=='0':
                    count+=1
            else:
                if aa[i]=='1' and bb[i]=='1':
                    count+=2
                elif (aa[i] == '1' and bb[i]=='0') or (aa[i]=='0' and bb[i]=='1'):
                    count+=1
        return count
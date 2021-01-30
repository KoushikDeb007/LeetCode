class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        count = 0
        for i in nums:
            if k-i in d:
                d[k-i]-=1
                if d[k-i]==0:
                    del d[k-i]
                count+=1
            else:
                d[i]+=1
        return count
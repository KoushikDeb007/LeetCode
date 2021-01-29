class Solution:
    def numTeams(self, rating: List[int]) -> int:
                ####### TLE NOW ######
        #         def dfs(prev, count, team, great):
        #             if team == 2:
        #                 return 1
        #             if prev==len(rating)-1:
        #                 return 0
        #             for i in range(prev + 1, len(rating), 1):

        #                 if great and rating[prev] < rating[i]:
        #                         count += dfs(i, 0, team + 1, great)

        #                 elif great==0 and rating[prev] > rating[i]:
        #                     count += dfs(i, 0, team + 1, great)
        #             return count

        #         count = 0
        #         for i in range(len(rating)):
        #             count += dfs(i, 0, 0, 1)
        #             count +=  dfs(i, 0, 0, 0)
        #         return count

        #         left_arr = []
        #         right_arr = sorted(rating)
        #         count = 0
        #         for soldier in rating:
        #             right_arr.remove(soldier)
        #             left_lo = bisect.bisect(left_arr, soldier)
        #             left_high = len(left_arr) - left_lo
        #             right_low = bisect.bisect(right_arr,soldier)
        #             right_high = len(right_arr) - right_low
        #             # print(right_arr)
        #             # print(left_lo,left_high,right_low,right_high,soldier)

        #             count = count + left_lo*right_high + left_high*right_low

        #             bisect.insort(left_arr, soldier)
        #         return count

        n = len(rating)
        dp = [[0 for i in range(3)] for i in range(n)]
        res = 0

        for i in range(n):
            dp[i][0] = 1
            for j in range(i):
                if rating[j] < rating[i]:
                    dp[i][1] += dp[j][0]
                    res += dp[j][1]
                if rating[j] > rating[i]:
                    dp[i][2] += dp[j][0]
                    res += dp[j][2]

        return res
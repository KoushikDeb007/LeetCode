class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        #         dp = [[0 for i in range(len(arr))] for j in range(len(arr))]
        #         for i in range(len(arr)):
        #             dp[i][i] = (0, arr[i])

        #         for v in range(1,len(arr)):
        #             for j in range(v, len(arr)):
        #                 i = j - v
        #                 D_i_j = min(dp[i][k][0] + dp[k+1][j][0] + dp[i][k][1] * dp[k+1][j][1] for k in range(i, j))
        #                 M_i_j = max(dp[i][j-1][1], arr[j])

        #                 dp[i][j] = (D_i_j, M_i_j)

        #         return dp[0][len(arr)-1][0]

        # res = 0
        # while len(arr) > 1:
        #     i = arr.index(min(arr))
        #     x = arr[i - 1:i] + arr[i + 1:i + 2]
        #     # print(x)
        #     res += min(x) * arr.pop(i)
        # return res
        stack = [float('inf')]
        res = 0

        for a in arr:
            while stack and stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
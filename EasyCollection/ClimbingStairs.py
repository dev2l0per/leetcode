class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 46

        dp[0] = 1
        dp[1] = 1
        for i in range(2, 46):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]
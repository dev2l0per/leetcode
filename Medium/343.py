class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)

        if n <= 3:
            return n - 1

        if n < 5:
            return n

        for i in range(5):
            dp[i] = i
        
        for i in range(5, n + 1):
            dp[i] = dp[i - 3] * 3
        return dp[n]
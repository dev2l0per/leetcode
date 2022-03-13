class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]

        for index in range(3, n + 1):
            dp.append(dp[index - 2] + dp[index - 1])
        
        return dp[n]

sol = Solution()
print(sol.climbStairs(3))
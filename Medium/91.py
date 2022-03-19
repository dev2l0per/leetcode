class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        dp = [0 for _ in range(length + 1)]

        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for index in range(2, length + 1):
            if s[index - 1] != '0':
                dp[index] = dp[index - 1]
            number = int(s[index - 2 : index])
            if number >= 10 and number <= 26:
                dp[index] += dp[index - 2]
        
        return dp[length]

sol = Solution()
print(sol.numDecodings("226"))
print(sol.numDecodings("10"))
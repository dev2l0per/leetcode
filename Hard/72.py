class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lengthOfWord1, lengthOfWord2 = len(word1), len(word2)

        if lengthOfWord1 == 0 or lengthOfWord2 == 0:
            return lengthOfWord1 + lengthOfWord2

        dp = [[0] * (lengthOfWord2 + 1) for _ in range(lengthOfWord1 + 1)]

        for i in range(lengthOfWord1 + 1):
            dp[i][0] = i
        for j in range(lengthOfWord2 + 1):
            dp[0][j] = j

        for i in range(1, lengthOfWord1 + 1):
            for j in range(1, lengthOfWord2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1
        return dp[lengthOfWord1][lengthOfWord2]

sol = Solution()
print(sol.minDistance("horse", "ros"))
print(sol.minDistance("intention", "execution"))
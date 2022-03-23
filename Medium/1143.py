class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lengthOfText1, lengthOfText2 = len(text1), len(text2)
        dp = [[0] * (lengthOfText2 + 1) for _ in range(lengthOfText1 + 1)]

        for i in range(1, lengthOfText1 + 1):
            for j in range(1, lengthOfText2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[lengthOfText1][lengthOfText2]

sol = Solution()
print(sol.longestCommonSubsequence("abcde", "ace"))
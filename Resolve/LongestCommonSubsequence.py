from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1Length: int = len(text1)
        text2Length: int = len(text2)
        dp: List[List[int]] = [[0 for _ in range(text2Length + 1)] for _ in range(text1Length + 1)]

        for i in range(1, text1Length + 1):
            for j in range(1, text2Length + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
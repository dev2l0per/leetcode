from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1Len: int = len(word1)
        word2Len: int = len(word2)

        dp: List[List[int]] = [[0 for _ in range(word2Len + 1)] for _ in range(word1Len + 1)]

        for i in range(1, word1Len + 1):
            for j in range(1, word2Len + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j - 1])
        return word1Len + word2Len - 2 * dp[-1][-1]
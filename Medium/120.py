from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        dp = [([triangle[0][0]] * n) for _ in range(n)]

        for rowIndex in range(1, n):
            dp[rowIndex][0] = dp[rowIndex - 1][0] + triangle[rowIndex][0]
            for colIndex in range(1, rowIndex):
                dp[rowIndex][colIndex] = min(dp[rowIndex - 1][colIndex - 1] + triangle[rowIndex][colIndex], dp[rowIndex - 1][colIndex] + triangle[rowIndex][colIndex])
            dp[rowIndex][rowIndex] = dp[rowIndex - 1][rowIndex - 1] + triangle[rowIndex][rowIndex]

        return min(dp[-1])

sol = Solution()
print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
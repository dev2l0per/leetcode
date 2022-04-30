# 1 4 9 16 25
# 1 2 3 1 2

from typing import List
import math

class Solution:
    def numSquares(self, n: int) -> int:
        squareList: List[int] = []
        dp: List[int] = [math.inf] * (n + 1)

        dp[0] = 0
        i: int = 1
        while i * i <= n:
            squareList.append(i * i)
            i += 1
        for index in range(1, n + 1):
            for square in squareList:
                if index < square:
                    break
                dp[index] = min(dp[index], dp[index - square] + 1)
        return dp[n]
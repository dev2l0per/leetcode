from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp: List[int] = [math.inf] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for value in range(coin, amount + 1):
                dp[value] = min(dp[value], dp[value - coin] + 1)
        if dp[-1] == math.inf:
            return -1
        return dp[-1]
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for value in range(coin, amount + 1):
                dp[value] = min(dp[value], dp[value - coin] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
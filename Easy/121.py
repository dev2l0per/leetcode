from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = 10 ** 4
        result = 0
        for i in range(len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
                continue
            if result < prices[i] - buyPrice:
                result = prices[i] - buyPrice
        return result

sol = Solution()
print(sol.maxProfit([7, 6, 4, 3, 1]))
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 10**5 + 1
        result = 0
        for i in range(0, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                result = max(prices[i] - minPrice, result)
        return result
from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice: int = math.inf
        result: int = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                result = max(prices[i] - minPrice, result)
        return result
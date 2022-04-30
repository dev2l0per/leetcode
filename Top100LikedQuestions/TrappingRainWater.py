from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n: int = len(height)
        dpToLeft: List[int] = [0] * n
        dpToRight: List[int] = [0] * n
        result: int = 0

        maxHeight = 0
        for i in range(n):
            maxHeight = max(maxHeight, height[i])
            dpToLeft[i] = maxHeight
        maxHeight = 0
        for i in range(n - 1, -1, -1):
            maxHeight = max(maxHeight, height[i])
            dpToRight[i] = maxHeight
        for i in range(n):
            result += min(dpToRight[i], dpToLeft[i]) - height[i]
        return result
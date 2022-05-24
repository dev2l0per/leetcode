from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left: int = 0
        right: int = len(height) - 1
        result: int = 0

        while left < right:
            result = max(result, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        result = 0

        while start < end:
            result = max(result, min(height[start], height[end]) * (end - start))

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return result

sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
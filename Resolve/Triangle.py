from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m: int = len(triangle)
        
        for i in range(1, m):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] = min(triangle[i-1][j - 1], triangle[i - 1][j]) + triangle[i][j]
        return min(triangle[-1])
from typing import List
from collections import defaultdict
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = 1

        if len(points) < 3:
            return len(points)

        for i in range(len(points)):
            counter = defaultdict(lambda: 1)
            for j in range(len(points)):
                if i == j:
                    continue
                dx, dy = points[i][0] - points[j][0], points[i][1] - points[j][1]
                if dx == 0:
                    slope = (0, 1)
                elif dy == 0:
                    slope = (1, 0)
                else:
                    gcd = math.gcd(dx, dy)
                    slope = (dx // gcd, dy // gcd)
                counter[slope] += 1
            result = max(result, max(counter.values()))
        return result

sol = Solution()
print(sol.maxPoints([[1,1],[2,2],[3,3]]))
from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        queue = deque()
        directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

        queue.append((0, 0, 1))
        grid[0][0] = 1

        while queue:
            cur = queue.popleft()

            if cur[0] == n - 1 and cur[1] == n - 1:
                return cur[2]
            for direction in directions:
                if 0 <= cur[0] + direction[0] and cur[0] + direction[0] < n and 0 <= cur[1] + direction[1] and cur[1] + direction[1] < n:
                    if grid[cur[0] + direction[0]][cur[1] + direction[1]] == 0:
                        queue.append((cur[0] + direction[0], cur[1] + direction[1], cur[2] + 1))
                        grid[cur[0] + direction[0]][cur[1] + direction[1]] = 1
            
        return -1

sol = Solution()
print(sol.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
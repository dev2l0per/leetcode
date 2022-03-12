from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = ((-1, 0), (0, 1), (1, 0), (0, -1))
        m, n, freshOrangeCount = len(grid), len(grid[0]), 0
        queue = deque()
        result = 0

        for rowIndex in range(m):
            for colIndex in range(n):
                if grid[rowIndex][colIndex] == 2:
                    queue.append((rowIndex, colIndex))
                elif grid[rowIndex][colIndex] == 1:
                    freshOrangeCount += 1
        
        queue.append((-1, -1))

        while queue:
            x, y = queue.popleft()
            if x == -1 and y == -1:
                if queue:
                    result += 1
                    queue.append((-1, -1))

            for dir in direction:
                if x + dir[0] < 0 or x + dir[0] >= m or y + dir[1] < 0 or y + dir[1] >= n:
                    continue
                if grid[x + dir[0]][y + dir[1]] == 1:
                    grid[x + dir[0]][y + dir[1]] = 2
                    queue.append((x + dir[0], y + dir[1]))
                    freshOrangeCount -= 1
        
        if freshOrangeCount != 0:
            return -1
        return result

sol = Solution()
print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m, n, result = len(grid), len(grid[0]), 0
        
        for rowIndex in range(m):
            for colIndex in range(n):
                if grid[rowIndex][colIndex] == 0:
                    continue

                count = 0
                bfsQueue = deque()
                bfsQueue.append((rowIndex, colIndex))
                grid[rowIndex][colIndex] = 0

                while bfsQueue:
                    cur = bfsQueue.popleft()

                    for curDirection in direction:
                        if cur[0] + curDirection[0] < 0 or cur[0] + curDirection[0] >= m or cur[1] + curDirection[1] < 0 or cur[1] + curDirection[1] >= n:
                            continue
                        if grid[cur[0] + curDirection[0]][cur[1] + curDirection[1]] == 1:
                            bfsQueue.append((cur[0] + curDirection[0], cur[1] + curDirection[1]))
                            grid[cur[0] + curDirection[0]][cur[1] + curDirection[1]] = 0
                    count += 1
                result = max(result, count)
        
        return result

sol = Solution()
print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(sol.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
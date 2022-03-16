from typing import List
from collections import deque

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         queue = deque()
#         m, n = len(grid), len(grid[0])
#         result = 0

#         for row in range(m):
#             for col in range(n):
#                 if grid[row][col] == "1":
#                     result += 1
#                     queue.append([row, col])

#                     while queue:
#                         cur = queue.popleft()

#                         if cur[0] > 0 and grid[cur[0] - 1][cur[1]] == "1":
#                             queue.append([cur[0] - 1, cur[1]])
#                             grid[cur[0] - 1][cur[1]] = "0"
#                         if cur[0] < m - 1 and grid[cur[0] + 1][cur[1]] == "1":
#                             queue.append([cur[0] + 1, cur[1]])
#                             grid[cur[0] + 1][cur[1]] = "0"
#                         if cur[1] > 0 and grid[cur[0]][cur[1] - 1] == "1":
#                             queue.append([cur[0], cur[1] - 1])
#                             grid[cur[0]][cur[1] - 1] = "0"
#                         if cur[1] < n - 1 and grid[cur[0]][cur[1] + 1] == "1":
#                             queue.append([cur[0], cur[1] + 1])
#                             grid[cur[0]][cur[1] + 1] = "0"
        
#         return result

sol = Solution()
print(sol.numIslands(grid = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
    ]))
from typing import List, Deque, Tuple
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions: Tuple[Tuple] = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m: int = len(grid)
        n: int = len(grid[0])
        result: int = 0
        def bfs(row: int, col: int) -> None:
            queue: Deque = deque()

            queue.append((row, col))
            grid[row][col] = "0"
            while queue:
                cur: Tuple[int, int] = queue.popleft()

                for direction in directions:
                    nextRow: int = cur[0] + direction[0]
                    nextCol: int = cur[1] + direction[1]

                    if 0 <= nextRow and nextRow < m and 0 <= nextCol and nextCol < n and grid[nextRow][nextCol] == "1":
                        queue.append((nextRow, nextCol))
                        grid[nextRow][nextCol] = "0"
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    result += 1
        return result
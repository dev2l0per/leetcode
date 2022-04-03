from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        m = len(rooms)
        if m <= 0:
            return
        n = len(rooms[0])

        queue = deque()
        direction = [
            [-1, 0, 1, 0],
            [0, 1, 0, -1],
        ]

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            cur = queue.popleft()

            for i in range(4):
                if cur[0] + direction[0][i] < 0 or cur[1] + direction[1][i] < 0 or cur[0] + direction[0][i] >= m or cur[1] + direction[1][i] >= n:
                    continue
                if rooms[cur[0] + direction[0][i]][cur[1] + direction[1][i]] == INF:
                    rooms[cur[0] + direction[0][i]][cur[1] + direction[1][i]] = rooms[cur[0]][cur[1]] + 1
                    queue.append((cur[0] + direction[0][i], cur[1] + direction[1][i]))
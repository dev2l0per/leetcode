from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        if m <= 0 :
            return [[]]
        n = len(heights[0])

        directions = [
            [-1, 0, 1, 0],
            [0, 1, 0, -1],
        ]

        pacificQueue = deque()
        pacificReachable = set()
        atlanticQueue = deque()
        atlanticReachable = set()
        
        for i in range(m):
            pacificQueue.append((i, 0))
            atlanticQueue.append((i, n - 1))
        for i in range(n):
            pacificQueue.append((0, i))
            atlanticQueue.append((m - 1, i))
        
        while pacificQueue:
            row, col = pacificQueue.popleft()
            pacificReachable.add((row, col))

            for direction in range(4):
                r = row + directions[0][direction]
                c = col + directions[1][direction]
                if r < 0 or r >= m or c < 0 or c >= n:
                    continue
                if (r, c) in pacificReachable:
                    continue
                if heights[row][col] <= heights[r][c]:
                    pacificQueue.append((r, c))
        while atlanticQueue:
            row, col = atlanticQueue.popleft()
            atlanticReachable.add((row, col))

            for direction in range(4):
                r = row + directions[0][direction]
                c = col + directions[1][direction]
                if r < 0 or r >= m or c < 0 or c >= n:
                    continue
                if (r, c) in atlanticReachable:
                    continue
                if heights[row][col] <= heights[r][c]:
                    atlanticQueue.append((r, c))
        return list(pacificReachable.intersection(atlanticReachable))
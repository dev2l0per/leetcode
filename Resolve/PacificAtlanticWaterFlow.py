from typing import List, Deque, Tuple, Set
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m: int = len(heights)
        n: int = len(heights[0])

        directions: Tuple[Tuple] = ((0, 1), (1, 0), (0, -1), (-1, 0))

        pacificQueue: Deque = deque()
        atlanticQueue: Deque = deque()
        
        pacificReachable: Set = set()
        atlanticReachable: Set = set()

        for i in range(m):
            pacificQueue.append((i, 0))
            atlanticQueue.append((i, n - 1))
        for i in range(n):
            pacificQueue.append((0, i))
            atlanticQueue.append((m - 1, i))
        while pacificQueue:
            curRow: int
            curCol: int
            curRow, curCol = pacificQueue.popleft()
            pacificReachable.add((curRow, curCol))

            for direction in directions:
                nextRow: int = curRow + direction[0]
                nextCol: int = curCol + direction[1]

                if not (0 <= nextRow and nextRow < m and 0 <= nextCol and nextCol < n):
                    continue
                if (nextRow, nextCol) in pacificReachable:
                    continue
                if heights[curRow][curCol] <= heights[nextRow][nextCol]:
                    pacificQueue.append((nextRow, nextCol))
        while atlanticQueue:
            curRow: int
            curCol: int
            curRow, curCol = atlanticQueue.popleft()
            atlanticReachable.add((curRow, curCol))

            for direction in directions:
                nextRow: int = curRow + direction[0]
                nextCol: int = curCol + direction[1]

                if not (0 <= nextRow and nextRow < m and 0 <= nextCol and nextCol < n):
                    continue
                if (nextRow, nextCol) in atlanticReachable:
                    continue
                if heights[curRow][curCol] <= heights[nextRow][nextCol]:
                    atlanticQueue.append((nextRow, nextCol))
        return list(pacificReachable.intersection(atlanticReachable))
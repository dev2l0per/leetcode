from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        direction = ((-1, 0), (0, 1), (1, 0), (0, -1))
        queue = deque()
        result = [[0] * n for _ in range(m)]
        
        for rowIndex in range(m):
            for colIndex in range(n):
                if mat[rowIndex][colIndex] == 0:
                    queue.append((rowIndex, colIndex))
                else:
                    result[rowIndex][colIndex] = 2147483647
        
        while queue:
            curPosition = queue.popleft()

            for curDirection in direction:
                if curPosition[0] + curDirection[0] < 0 or curPosition[0] + curDirection[0] >= m or curPosition[1] + curDirection[1] < 0 or curPosition[1] + curDirection[1] >= n:
                    continue
                if result[curPosition[0] + curDirection[0]][curPosition[1] + curDirection[1]] > result[curPosition[0]][curPosition[1]] + 1:
                    result[curPosition[0] + curDirection[0]][curPosition[1] + curDirection[1]] = result[curPosition[0]][curPosition[1]] + 1
                    queue.append((curPosition[0] + curDirection[0], curPosition[1] + curDirection[1]))
        return result
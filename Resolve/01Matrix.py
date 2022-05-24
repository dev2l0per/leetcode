from typing import List, Deque, Tuple
from collections import deque
import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m: int = len(mat)
        n: int = len(mat[0])
        queue: Deque = deque()
        directions: Tuple[Tuple] = ((0, 1), (1, 0), (0, -1), (-1, 0))

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = math.inf
        
        while queue:
            curRow: int
            curCol: int
            curRow, curCol = queue.popleft()

            for direction in directions:
                nextRow: int = curRow + direction[0]
                nextCol: int = curCol + direction[1]

                if 0 > nextRow or m <= nextRow or 0 > nextCol or n <= nextCol:
                    continue
                if mat[nextRow][nextCol] > mat[curRow][curCol] + 1:
                    mat[nextRow][nextCol] = mat[curRow][curCol] + 1
                    queue.append((nextRow, nextCol))
        return mat
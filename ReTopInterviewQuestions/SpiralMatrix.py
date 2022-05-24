from typing import List, Tuple

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED: int = 101
        directions: Tuple = ((0, 1), (1, 0), (0, -1), (-1, 0))
        result: List[int] = []
        m: int = len(matrix)
        n: int = len(matrix[0])

        curRow: int = 0
        curCol: int = 0
        curDir: int = 0
        while True:
            result.append(matrix[curRow][curCol])
            matrix[curRow][curCol] = VISITED
            if 0 > curRow + directions[curDir][0] or curRow + directions[curDir][0] >= m or 0 > curCol + directions[curDir][1] or curCol + directions[curDir][1] >= n or matrix[curRow + directions[curDir][0]][curCol + directions[curDir][1]] == VISITED:
                curDir = (curDir + 1) % 4
            curRow = curRow + directions[curDir][0]
            curCol = curCol + directions[curDir][1]
            if 0 > curRow or curRow >= m or 0 > curCol or curCol >= n or matrix[curRow][curCol] == VISITED:
                break
        return result
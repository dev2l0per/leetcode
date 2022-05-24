from typing import List, Tuple

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions: Tuple[Tuple[int, int]] = ((0, 1), (1, 0), (0, -1), (-1, 0))
        result: List[int] = []
        m: int = len(matrix)
        n: int = len(matrix[0])
        VISIT: int = 101

        curRow: int = 0
        curCol: int = 0
        curDirection = 0
        while True:
            result.append(matrix[curRow][curCol])
            matrix[curRow][curCol] = VISIT
            nextRow: int = curRow + directions[curDirection][0]
            nextCol: int = curCol + directions[curDirection][1]

            if nextRow >= m or nextCol >= n or matrix[nextRow][nextCol] == VISIT:
                curDirection = (curDirection + 1) % 4
            curRow = curRow + directions[curDirection][0]
            curCol = curCol + directions[curDirection][1]
            if curRow >= m or curCol >= n or matrix[curRow][curCol] == VISIT:
                break
        return result
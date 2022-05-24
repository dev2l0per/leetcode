from typing import List, Set

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        checkRow: Set = set()
        checkCol: Set = set()
        m: int = len(matrix)
        n: int = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    checkRow.add(i)
                    checkCol.add(j)
        for row in checkRow:
            for i in range(n):
                matrix[row][i] = 0
        for col in checkCol:
            for i in range(m):
                matrix[i][col] = 0
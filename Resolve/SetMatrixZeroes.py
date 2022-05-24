from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        checkRow, checkCol = set(), set()
        m, n = len(matrix), len(matrix[0])

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
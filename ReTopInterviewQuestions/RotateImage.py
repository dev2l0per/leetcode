from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m: int = len(matrix)
        n: int = len(matrix[0])

        for i in range(m // 2):
            for j in range(n):
                matrix[i][j], matrix[m - 1 - i][j] = matrix[m - 1 - i][j], matrix[i][j]
        for i in range(m):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
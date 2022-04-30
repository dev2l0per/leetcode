from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None:
            return False

        m: int = len(matrix)
        n: int = len(matrix[0])
        row: int = 0
        col: int = n - 1

        while row < m and col >= 0 and col < n:
            if matrix[row][col] < target:
                row += 1
            else:
                if matrix[row][col] == target:
                    return True
                else:
                    col -= 1
        return False
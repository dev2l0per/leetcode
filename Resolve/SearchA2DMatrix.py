from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(rowStart, colStart, rowEnd, colEnd) -> bool:
            if rowStart > rowEnd:
                return False
            if colStart > colEnd:
                return False
            rowMid: int = (rowStart + rowEnd) // 2
            colMid: int = (colStart + colEnd) // 2

            if matrix[rowMid][colMid] == target:
                return True
            elif matrix[rowMid][colMid] > target:
                return binarySearch(rowStart, colStart, rowMid - 1, colEnd) or \
                    binarySearch(rowMid, colStart, rowMid, colMid - 1)
            else:
                return binarySearch(rowMid + 1, colStart, rowEnd, colEnd) or \
                    binarySearch(rowMid, colMid + 1, rowMid, colEnd)
        return binarySearch(0, 0, len(matrix) - 1, len(matrix[0]) - 1)
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(startX: int, startY: int, endX: int, endY: int) -> bool:
            if startX > endX or startY > endY:
                return False
            midX: int = (startX + endX) // 2
            midY: int = (startY + endY) // 2

            if matrix[midY][midX] == target:
                return True
            elif matrix[midY][midX] > target:
                return search(startX, startY, endX, midY - 1) or search(startX, startY, midX - 1, endY)
            return search(startX, midY + 1, endX, endY) or search(midX + 1, startY, endX, endY)
        return search(0, 0, len(matrix[0]) - 1, len(matrix) - 1)
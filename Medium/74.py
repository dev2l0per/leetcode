from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m - 1

        while left <= right:
            mid = int((left + right) / 2)

            if matrix[mid][0] <= target:
                left = mid + 1
            else:
                right = mid - 1
        rowIndex = right

        left, right = 0, n - 1
        while left <= right:
            mid = int((left + right) / 2)

            if matrix[rowIndex][mid] == target:
                return True
            elif matrix[rowIndex][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
print(sol.searchMatrix([[1,3]], 3))
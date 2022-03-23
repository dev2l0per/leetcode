from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])

        left, right = 0, n - 1
        while left <= right:
            pivot = int((left + right) / 2)
            maxValue = -1

            for i in range(m):
                if maxValue < mat[pivot][i]:
                    maxValue = mat[pivot][i]
                    col = i
            
            leftIsBig = pivot - 1 >= left and mat[pivot - 1][col] > mat[pivot][col]
            rightIsBig = pivot + 1 <= right and mat[pivot + 1][col] > mat[pivot][col]
            
            if not leftIsBig and not rightIsBig:
                return [pivot, col]
            elif rightIsBig: 
                left = pivot + 1
            else:
                right = pivot - 1

        return []

sol = Solution()
print(sol.findPeakGrid([[1, 4], [3, 2]]))
print(sol.findPeakGrid([[10, 20, 15], [21, 30, 14], [7, 16, 32]]))
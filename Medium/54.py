from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        CHECK = 200
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        result = []
        m, n = len(matrix), len(matrix[0])

        curRow, curCol, curDirection = 0, 0, 0
        while True:
            result.append(matrix[curRow][curCol])
            matrix[curRow][curCol] = CHECK
            if (curRow + directions[curDirection][0] >= m or curCol + directions[curDirection][1] >= n) or (matrix[curRow + directions[curDirection][0]][curCol + directions[curDirection][1]] == CHECK):
                curDirection = (curDirection + 1) % 4
            curRow, curCol = curRow + directions[curDirection][0], curCol + directions[curDirection][1]
            if (curRow >= m or curCol >= n) or matrix[curRow][curCol] == CHECK:
                break
        return result

sol = Solution()
print(sol.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(sol.spiralOrder([[1]]))
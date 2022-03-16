from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])
        queue = deque()
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        from itertools import product

        borders = list(product(range(m), [0, n - 1])) + list(product([0, m - 1], range(n)))

        for border in borders:
            queue.append(border)

            while queue:
                cur = queue.popleft()

                if board[cur[0]][cur[1]] != 'O':
                    continue
                board[cur[0]][cur[1]] = 'E'

                for direction in directions:
                    if 0 < cur[0] + direction[0] and cur[0] + direction[0] < m - 1 and 0 < cur[1] + direction[1] and cur[1] + direction[1] < n - 1:
                        queue.append((cur[0] + direction[0], cur[1] + direction[1]))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'
        print(board)

sol = Solution()
sol.solve([["O","O","O"],["O","O","O"],["O","O","O"]])
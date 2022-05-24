from typing import List, Tuple

class Solution:
    def exist(self, board: List[List[int]], word: str) -> bool:
        directions: Tuple = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m: int = len(board)
        n: int = len(board[0])

        def backtrack(combination: List[str], row: int, col: int) -> bool:
            if board[row][col] == "":
                return False
            if board[row][col] == word[len(combination)]:
                combination.append(board[row][col])
                if len(combination) == len(word):
                    return True
                board[row][col] = ""
                for direction in directions:
                    nextRow: int = row + direction[0]
                    nextCol: int = col + direction[1]
                    if 0 <= nextRow and nextRow < m and 0 <= nextCol and nextCol < n:
                        if backtrack(combination, nextRow, nextCol):
                            return True
                board[row][col] = combination.pop()
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack([], i, j):
                        return True
        return False
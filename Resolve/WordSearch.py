from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        def backtrack(combination: List[str], row: int, col: int):
            if board[row][col] == "":
                return False
            if board[row][col] == word[len(combination)]:
                combination.append(board[row][col])
                if len(combination) == len(word):
                    return True
                board[row][col] = ""
                for direction in directions:
                    if row + direction[0] >= 0 and row + direction[0] < len(board) and col + direction[1] >= 0 and col + direction[1] < len(board[0]):
                        if (backtrack(combination, row + direction[0], col + direction[1])):
                            return True
                board[row][col] = combination.pop()
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if (backtrack([], i, j)):
                        return True
        
        return False
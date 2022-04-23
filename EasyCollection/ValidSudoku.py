from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        squareSet = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rowSet[i] or board[i][j] in colSet[j] or board[i][j] in squareSet[i // 3 * 3 + j // 3]:
                    return False
                rowSet[i].add(board[i][j])
                colSet[j].add(board[i][j])
                squareSet[i // 3 * 3 + j // 3].add(board[i][j])
        return True
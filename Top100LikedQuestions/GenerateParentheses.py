from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: List[str] = []

        def backtrack(parentheses: List[str], openCnt: int, closeCnt: int) -> None:
            if len(parentheses) == n * 2:
                result.append(''.join(parentheses))
                return
            if openCnt < n:
                parentheses.append('(')
                backtrack(parentheses, openCnt + 1, closeCnt)
                parentheses.pop()
            if closeCnt < openCnt:
                parentheses.append(')')
                backtrack(parentheses, openCnt, closeCnt + 1)
                parentheses.pop()
        backtrack([], 0, 0)
        return result
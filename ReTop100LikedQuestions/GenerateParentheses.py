from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: List[str] = []

        def backtrack(arr: List[str], openCnt: int, closeCnt: int) -> None:
            if len(arr) == n * 2:
                result.append(''.join(arr))
                return
            if openCnt < n:
                arr.append('(')
                backtrack(arr, openCnt + 1, closeCnt)
                arr.pop()
            if closeCnt < openCnt:
                arr.append(')')
                backtrack(arr, openCnt, closeCnt + 1)
                arr.pop()
        backtrack([], 0, 0)
        return result
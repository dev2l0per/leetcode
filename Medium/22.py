from typing import List
from xmlrpc.client import boolean

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(combination: List[str], openCnt: int, closeCnt: int):
            if len(combination) == n * 2:
                result.append("".join(combination))
                return
            if openCnt < n:
                combination.append("(")
                backtrack(combination, openCnt + 1, closeCnt)
                combination.pop()
            if openCnt > closeCnt:
                combination.append(")")
                backtrack(combination, openCnt, closeCnt + 1)
                combination.pop()
        backtrack([], 0, 0)
        return result

sol = Solution()
print(sol.generateParenthesis(3))
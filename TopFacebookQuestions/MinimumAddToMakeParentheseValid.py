class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openCnt: int = 0
        result: int = 0

        for ch in s:
            if ch == '(':
                openCnt += 1
            else:
                if openCnt == 0:
                    result += 1
                else:
                    openCnt -= 1
        return result + openCnt
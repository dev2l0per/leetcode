from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length: int = len(temperatures)
        dp: List[int] = [0] * length
        check: int = 0

        for i in range(length - 1, -1, -1):
            if temperatures[i] >= check:
                check = temperatures[i]
                continue
            j: int = 1
            while temperatures[i + j] <= temperatures[i]:
                j += dp[i + j]
            dp[i] = j
        return dp
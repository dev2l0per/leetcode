# 0 1 1 2 1 2 2 3 1 2 2 3 2 3 3 4
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] = dp[i - (i & ( -i ))] + 1
        return dp
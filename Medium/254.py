import math
from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []

        def dfs(arr: List[int], number, div):
            if len(arr) >= 1:
                result.append(arr + [number])
            for i in range(div, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    arr.append(i)
                    dfs(arr, number // i, i)
                    arr.remove(i)

        dfs([], n, 2)
        return result
sol = Solution()
print(sol.getFactors(1))
print(sol.getFactors(12))
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(combination: List[int], startIndex: int, curSum: int) -> None:
            if len(combination) > k:
                return
            if curSum == n and len(combination) == k:
                result.append(combination[:])
                return
            for i in range(startIndex, 10):
                combination.append(i)
                backtrack(combination, startIndex + 1, curSum + i)
                combination.pop()
        backtrack([], 1, 0)
        return result
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(arr: List[int], sum: int, startIndex: int) -> None:
            if sum == target:
                result.append(arr[:])
                return
            if sum > target:
                return
            for i in range(startIndex, len(candidates)):
                arr.append(candidates[i])
                backtrack(arr, sum + candidates[i], i)
                arr.pop()
        backtrack([], 0, 0)
        return result
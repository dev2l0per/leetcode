from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result: List[List[int]] = []

        def backtrack(arr: List[int], sum: int, startIndex: int) -> None:
            if sum == target:
                result.append(arr[:])
                return
            if sum > target:
                return
            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                backtrack(arr, sum + candidates[i], i + 1)
                arr.pop()
        backtrack([], 0, 0)
        return result
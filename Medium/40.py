from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def backtrack(combination: List[int], sum: int, index: int):
            if sum == target:
                result.append(combination[:])
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if sum + candidates[i] > target:
                    break
                combination.append(candidates[i])
                sum += candidates[i]
                backtrack(combination, sum, i + 1)
                sum -= candidates[i]
                combination.pop()
        
        backtrack([], 0, 0)
        return result

sol = Solution()
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
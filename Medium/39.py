from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(combination: List[int], sum: int, index):
            if sum > target:
                return
            if sum == target:
                result.append(combination[:])
                return
            for i in range(index, len(candidates)):
                combination.append(candidates[i])
                sum += candidates[i]
                backtrack(combination, sum, i)
                sum -= candidates[i]
                combination.pop()
        
        backtrack([], 0, 0)
        return result

sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
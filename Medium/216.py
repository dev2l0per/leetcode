from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(combination: List[int], index: int, sum: int):
            if sum > n:
                return
            if len(combination) == k and sum == n:
                result.append(combination[:])
            for i in range(index, 10):
                combination.append(i)
                sum += i
                backtrack(combination, i + 1, sum)
                sum -= i
                combination.pop()
        
        backtrack([], 1, 0)
        return result
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: List[List[int]] = []
        
        def backtrack(arr: List[int], cur: int):
            if len(arr) == k:
                result.append(arr[:])
                return
            for i in range(cur, n + 1):
                arr.append(i)
                backtrack(arr, i + 1)
                arr.pop()
        backtrack([], 1)
        return result
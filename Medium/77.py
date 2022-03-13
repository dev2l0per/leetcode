from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(cur, arr: List[int]):
            if len(arr) == k:
                result.append(arr[:])
            for index in range(cur, n + 1):
                arr.append(index)
                backtrack(index + 1, arr)
                arr.pop()
        result = []
        backtrack(1, [])
        
        return result

sol = Solution()
print(sol.combine(4, 2))
from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        result = []
        for i in range(m):
            result.append(original[i * n:i*n+n])
        return result

sol = Solution()
print(sol.construct2DArray([1,2,3,4], 2, 2))
print(sol.construct2DArray([1,2,3], 1, 3))
print(sol.construct2DArray([1,2], 1, 1))
print(sol.construct2DArray([3], 1, 2))
print(sol.construct2DArray([1, 1, 1, 1], 4, 1))
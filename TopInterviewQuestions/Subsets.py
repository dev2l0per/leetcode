from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[int] = []
        
        def backtrack(arr: List[int], start: int):
            result.append(arr[:])
            for i in range(start, len(nums)):
                arr.append(nums[i])
                backtrack(arr, i + 1)
                arr.pop()
        backtrack([], 0)
        return result
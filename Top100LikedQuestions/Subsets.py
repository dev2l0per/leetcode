from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        numsLength: int = len(nums)

        def backtrack(arr: List[int], startIndex: int):
            result.append(arr[:])
            for i in range(startIndex, numsLength):
                arr.append(nums[i])
                backtrack(arr, i + 1)
                arr.pop()
        backtrack([], 0)
        return result
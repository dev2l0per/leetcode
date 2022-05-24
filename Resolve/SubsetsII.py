from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        nums.sort()

        def backtrack(arr: List[int], startIndex: int) -> None:
            result.append(arr[:])
            for i in range(startIndex, len(nums)):
                if i != startIndex and nums[i] == nums[i - 1]:
                    continue
                arr.append(nums[i])
                backtrack(arr, i + 1)
                arr.pop()
        
        backtrack([], 0)
        return result
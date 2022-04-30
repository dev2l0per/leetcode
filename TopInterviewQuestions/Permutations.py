from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(startIndex: int):
            if startIndex == len(nums):
                result.append(nums[:])
                return
            for i in range(startIndex, len(nums)):
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
                backtrack(startIndex + 1)
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
        
        backtrack(0)
        return result
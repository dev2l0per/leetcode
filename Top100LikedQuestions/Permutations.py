from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        numLength: int = len(nums)

        def backtrack(startIndex: int):
            if startIndex == numLength:
                result.append(nums[:])
                return
            for i in range(startIndex, numLength):
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
                backtrack(startIndex + 1)
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
        
        backtrack(0)
        return result
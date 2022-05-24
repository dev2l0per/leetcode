from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result: List[int] = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        save: int = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * save
            save *= nums[i]
        return result
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur: int = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur], nums[i] = nums[i], nums[cur]
                cur += 1
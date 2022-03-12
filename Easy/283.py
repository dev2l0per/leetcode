from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[idx], nums[cur] = nums[cur], nums[idx]
                idx = idx + 1
        print(nums)

sol = Solution()
sol.moveZeroes([0, 1, 0, 3, 12])
sol.moveZeroes([2, 1])
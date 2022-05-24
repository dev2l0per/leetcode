from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instaed.
        """
        cur0: int = 0
        cur2: int = len(nums) - 1
        cur: int = 0

        while cur <= cur2:
            if nums[cur] == 0:
                nums[cur0], nums[cur] = nums[cur], nums[cur0]
                cur0 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[cur2] = nums[cur2], nums[cur]
                cur2 -= 1
            else:
                cur += 1
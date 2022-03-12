from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead
        """
        p1 = 0
        p2 = len(nums) - k % len(nums)
        nums[:] = nums[p2:] + nums[p1:p2]
        print(nums)

sol = Solution()
print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(sol.rotate([-1, -100, 3, 99], 2))
print(sol.rotate([1, 2], 5)) 
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l: int = 0
        r: int = len(nums) - 1

        while l < r:
            mid: int = (l + r) // 2

            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return r
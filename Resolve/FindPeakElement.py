from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binarySearch(l: int, r: int) -> int:
            if l >= r:
                return l
            mid: int = (l + r) // 2

            if nums[mid] > nums[mid + 1]:
                return binarySearch(l, mid)
            else:
                return binarySearch(mid + 1, r)
        return binarySearch(0, len(nums) - 1)
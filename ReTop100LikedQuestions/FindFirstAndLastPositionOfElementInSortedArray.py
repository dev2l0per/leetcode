from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left: int = 0
        right: int = len(nums) - 1
        lower: int = -1
        upper: int = -1

        while left <= right:
            mid: int = (left + right) // 2

            if nums[mid] == target:
                if mid == left or nums[mid - 1] < target:
                    lower = mid
                    break
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if lower == -1:
            return [lower, upper]
        left, right = lower, len(nums) - 1
        while left <= right:
            mid: int = (left + right) // 2

            if nums[mid] == target:
                if mid == right or nums[mid + 1] > target:
                    upper = mid
                    break
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [lower, upper]
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        start, end = 0, len(nums) - 1

        while start <= end:
            pivot = int((start + end) / 2)

            if nums[pivot] < target:
                start = pivot + 1
            else:
                end = pivot - 1
        lowerBound = start
        
        start, end = 0, len(nums) - 1
        while start <= end:
            pivot = int((start + end) / 2)

            if nums[pivot] <= target:
                start = pivot + 1
            else:
                end = pivot - 1
        upperBound = end

        if lowerBound > upperBound:
            return [-1, -1]

        return [lowerBound, upperBound]

sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
print(sol.searchRange([5, 8, 8, 9, 9, 10], 8))
print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))
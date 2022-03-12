from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            pivot = int((left + right) / 2)
            if nums[pivot] == target:
                return pivot
            if nums[left] <= nums[pivot]:
                if nums[left] <= target <= nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            else:
                if nums[pivot] <= target <= nums[right]:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return -1

sol = Solution()
print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))
print(sol.search([1, 3], 3))
print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))
print(sol.search([5, 1, 3], 5))
print(sol.search([5, 1, 3], 3))
print(sol.search([8, 1, 2, 3, 4, 5, 6, 7], 6))

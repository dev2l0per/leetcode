from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        pivot = 0

        if nums[len(nums) - 1] - nums[0] - (len(nums) - 1) < k:
            return nums[-1] + k - (nums[len(nums) - 1] - nums[0] - (len(nums) - 1))

        while left != right:
            pivot = int((left + right) / 2)

            if nums[pivot] - nums[0] - pivot < k:
                left = pivot + 1
            else:
                right = pivot
        return nums[left - 1] + k - (nums[left - 1] - nums[0] - (left - 1)) 

sol = Solution()
print(sol.missingElement([4, 7, 9, 10], 1))
print(sol.missingElement([4, 7, 9, 10], 3))
print(sol.missingElement([1, 2, 4], 3))
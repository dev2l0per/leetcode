from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = int((left + right) / 2)
            
            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1

sol = Solution()
# print(sol.search([-1, 0, 3, 5, 9, 12], 9))
# print(sol.search([-1, 0, 3, 5, 9, 12], 2))
print(sol.search([5], 5))
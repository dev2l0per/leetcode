from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p1 = 0
        p2 = len(nums) - 1
        length = len(nums)
        result = [0] * length

        for index in range(length - 1, -1, -1):
            p1Square = nums[p1] ** 2
            p2Square = nums[p2] ** 2

            if p1Square > p2Square:
                result[index] = p1Square
                p1 = p1 + 1
            else:
                result[index] = p2Square
                p2 = p2 - 1
        
        return result

sol = Solution()
print(sol.sortedSquares([-4, -1, 0, 3, 10]))
print(sol.sortedSquares([-7, -3, 2, 3, 11]))
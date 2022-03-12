from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        temp = 1
        for i in range(1, len(nums)):
            result[i] = nums[i - 1] * temp
            temp = temp * nums[i - 1]
        
        temp = 1
        for i in range(len(nums) - 2, -1, -1):
            temp = temp * nums[i + 1]
            result[i] = result[i] * temp
        return result

sol = Solution()
print(sol.productExceptSelf([-1, 1, 0, -3, 3]))
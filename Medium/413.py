from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        result = 0

        if length <= 2:
            return result
        
        dp = [0] * length

        for index in range(2, length):
            if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]:
                dp[index] = dp[index - 1] + 1
                result += dp[index]
        
        return result

sol = Solution()
print(sol.numberOfArithmeticSlices([1, 2, 3, 4]))
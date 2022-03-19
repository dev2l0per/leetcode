from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [length - 1] * length
        dp[0] = 0

        for i in range(length):
            jumpRange = min(i + nums[i], length - 1)
            for j in range(i, jumpRange + 1):
                dp[j] = min(dp[i] + 1, dp[j])
        
        return dp[length - 1]

sol = Solution()
print(sol.jump([2, 3, 1, 1, 4]))
print(sol.jump([2, 3, 0, 1, 4]))
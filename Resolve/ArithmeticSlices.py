from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length: int = len(nums)
        dp: List[int] = [0] * length

        if length < 3:
            return 0
        for i in range(2, length):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)
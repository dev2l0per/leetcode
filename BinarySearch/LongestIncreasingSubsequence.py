from typing import List

class Solution:
    def lengthOfLIS(slef, nums: List[int]) -> int:
        dp: List[int] = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
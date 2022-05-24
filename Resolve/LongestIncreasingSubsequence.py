from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length: int = len(nums)
        dp: List[int] = [1] * length

        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
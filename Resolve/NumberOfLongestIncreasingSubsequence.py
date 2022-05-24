from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n: int = len(nums)
        dp: List[int] = [1] * n
        count: List[int] = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] == dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        maxLength = max(dp)
        return sum([count[i] for i in range(n) if dp[i] == maxLength])
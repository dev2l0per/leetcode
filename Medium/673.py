from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        count = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] == dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        maxLength = max(dp)
        return sum([count[i] for i in range(len(nums)) if dp[i] == maxLength])

sol = Solution()
print(sol.findNumberOfLIS([1, 3, 5, 4, 7]))
print(sol.findNumberOfLIS([2, 2, 2, 2, 2]))
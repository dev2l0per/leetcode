from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        result, resultPrev = nums[0], 0

        for index in range(1, n):
            result, resultPrev = max(result, resultPrev + nums[index]), result
        
        return result

sol = Solution()
print(sol.rob([1, 2, 3, 1]))
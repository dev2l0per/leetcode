from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxRes = minRes = res = nums[0]
        for i in range(1, len(nums)):
            tempMax = maxRes * nums[i]
            tempMin = minRes * nums[i]
            maxRes = max(nums[i], tempMax, tempMin)
            minRes = min(nums[i], tempMax, tempMin)
            res = max(res, maxRes)
        return res

sol = Solution()
print(sol.maxProduct([-4, -3, -2]))
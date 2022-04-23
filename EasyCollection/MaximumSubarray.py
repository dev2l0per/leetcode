from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]):
        currentSum = maxSum = nums[0]

        for num in nums[1:]:
            currentSum = max(currentSum + num, num)
            maxSum = max(currentSum, maxSum)
        return maxSum
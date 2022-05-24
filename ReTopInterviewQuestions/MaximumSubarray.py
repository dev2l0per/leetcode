from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum: int = nums[0]
        result: int = nums[0]

        for num in nums[1:]:
            currentSum = max(currentSum + num, num)
            result = max(result, currentSum)
        return result
        
        # result: int = -math.inf

        # for i in range(len(nums)):
        #     temp: int = 0
        #     for j in range(i, len(nums)):
        #         temp += nums[j]
        #         result = max(result, temp)
        # return result
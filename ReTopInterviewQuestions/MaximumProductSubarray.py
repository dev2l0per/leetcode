from typing import List
import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxResult: int = nums[0]
        minResult: int = nums[0]
        result: int = nums[0]

        for num in nums[1:]:
            tempMax: int = max(num, max(maxResult * num, minResult * num))
            minResult = min(num, min(maxResult * num, minResult * num))
            maxResult = tempMax
            result = max(maxResult, result)
        return result
        
        
        # result: int = -math.inf

        # for i in range(len(nums)):
        #     temp: int = 1
        #     for j in range(i, len(nums)):
        #         temp *= nums[j]
        #         result = max(result, temp)
        # return result
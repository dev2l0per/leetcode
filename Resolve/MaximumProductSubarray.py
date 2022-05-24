from typing import List

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
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count: int = 0
        result: int = 0

        for num in nums:
            if count == 0:
                result = num
            if result == num:
                count += 1
            else:
                count -= 1
        return result
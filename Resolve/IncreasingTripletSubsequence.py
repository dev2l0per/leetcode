from typing import List
import math

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minValue: int = math.inf
        minNextValue: int = math.inf

        for num in nums:
            if num <= minValue:
                minValue = num
            elif num <= minNextValue:
                minNextValue = num
            else:
                return True
        return False
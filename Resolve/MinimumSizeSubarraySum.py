from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length: int = len(nums)
        result: int = 10001

        left: int = 0
        right: int = 0
        saveSum: int = 0

        while right < length:
            saveSum += nums[right]
            
            while saveSum >= target:
                result = min(result, right - left + 1)
                saveSum -= nums[left]
                left += 1

            right += 1
        if result == 10001:
            return 0
        return result
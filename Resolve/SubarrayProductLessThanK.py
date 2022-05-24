from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        saveProduct: int = 1
        left: int = 0
        result: int = 0

        for right in range(n):
            saveProduct *= nums[right]
            while saveProduct >= k and left <= right:
                saveProduct /= nums[left]
                left += 1
            result += right - left + 1
        return result
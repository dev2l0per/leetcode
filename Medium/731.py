from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0
        
        numsLength = len(nums)
        left = 0
        product = 1
        result = 0

        for index in range(numsLength):
            product *= nums[index]
            while product >= k and left <= index:
                product /= nums[left]
                left += 1
            result += index - left + 1
        return result
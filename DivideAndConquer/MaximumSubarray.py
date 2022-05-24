from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divideAndConquer(left: int, right: int) -> int:
            if left > right:
                return -math.inf
            mid: int = (left + right) // 2
            cur: int = 0
            leftResult: int = 0
            rightResult: int = 0

            for i in range(mid - 1, left - 1, -1):
                cur += nums[i]
                leftResult = max(leftResult, cur)
            cur = 0
            for i in range(mid + 1, right + 1):
                cur += nums[i]
                rightResult = max(rightResult, cur)
            
            result: int = nums[mid] + leftResult + rightResult
            leftSub: int = divideAndConquer(left, mid - 1)
            rightSub: int = divideAndConquer(mid + 1, right)

            return max(result, leftSub, rightSub)
        return divideAndConquer(0, len(nums) - 1)
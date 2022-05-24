from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divideAndConquer(left: int, right: int) -> int:
            if left > right:
                return -math.inf
            mid: int = (left + right) // 2

            cur: int = 0
            bestLeft: int = 0

            for i in range(mid - 1, left - 1, -1):
                cur += nums[i]
                bestLeft = max(bestLeft, cur)
            
            cur = 0
            bestRight: int = 0

            for i in range(mid + 1, right + 1):
                cur += nums[i]
                bestRight = max(bestRight, cur)
            
            bestCombine: int = nums[mid] + bestLeft + bestRight

            leftSub: int = divideAndConquer(left, mid - 1)
            rightSub: int = divideAndConquer(mid + 1, right)

            return max(bestCombine, leftSub, rightSub)
        return divideAndConquer(0, len(nums) - 1)
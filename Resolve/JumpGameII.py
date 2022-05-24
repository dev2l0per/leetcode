from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        count: int = 0
        currMax: int = 0
        nextMax: int = 0

        for i in range(len(nums) - 1):
            nextMax = max(nextMax, nums[i] + i)

            if i == currMax:
                count += 1
                currMax = nextMax
        return count
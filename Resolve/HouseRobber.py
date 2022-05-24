from typing import List
import math

class Solution:
    def rob(self, nums: List[int]) -> int:
        length: int = len(nums)
        jump: int = 0
        noJump: int = nums[length - 1]

        for i in range(length - 2, -1, -1):
            current: int = max(noJump, jump + nums[i])
            jump = noJump
            noJump = current
        return noJump
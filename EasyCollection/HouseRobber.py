from typing import List
import math

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        jump, nojump = 0, nums[n - 1]

        for i in range(n - 2, -1, -1):
            current = max(nojump, jump + nums[i])
            jump = nojump
            nojump = current
        return nojump
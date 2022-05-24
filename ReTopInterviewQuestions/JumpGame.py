from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def canJumpFromPosition(position: int) -> bool:
            if position == len(nums) - 1:
                return True
            far: int = min(len(nums) - 1, position + nums[position])
            for i in range(position + 1, far + 1):
                if canJumpFromPosition(i):
                    return True
            return False
        return canJumpFromPosition(0)
        
        
        # last: int = len(nums) - 1
        # for i in range(len(nums) - 1, -1, -1):
        #     if i + nums[i] >= last:
        #         last = i
        # return last == 0
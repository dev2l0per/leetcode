from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        flag = [False] * len(nums)
        flag[len(nums) - 1] = True
        for i in range(len(nums) - 2, -1, -1):
            jumpRange = min(i + nums[i], len(nums) - 1)
            for jump in range(i + 1, jumpRange + 1):
                if flag[jump]:
                    flag[i] = True
                    break
        
        return flag[0]

sol = Solution()
print(sol.canJump([2, 3, 1, 1, 4]))
print(sol.canJump([3, 2, 1, 0, 4]))
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur: int = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[cur] = nums[i + 1]
                cur += 1
        return cur

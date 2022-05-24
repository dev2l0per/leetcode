from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cursor: int = 1
        for i in range(0, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[cursor] = nums[i + 1]
                cursor += 1
        return cursor
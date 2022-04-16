from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashSet = set(nums)

        for i in range(len(nums) + 1):
            if i not in hashSet:
                return i
        return len(nums)
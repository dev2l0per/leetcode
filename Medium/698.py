from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        allSum = sum(nums)
        n = len(nums)

        if allSum % k != 0:
            return False
        
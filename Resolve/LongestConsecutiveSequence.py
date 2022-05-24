from typing import List, Set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result: int = 0
        hash: Set[int] = set(nums)

        for num in nums:
            if num - 1 not in hash:
                length = 1
                cur = num
                while cur + 1 in hash:
                    cur += 1
                    length += 1
                result = max(result, length)
        return result
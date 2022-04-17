from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        hashSet = set(nums)

        for num in nums:
            if num - 1 not in hashSet:
                length = 1
                cur = num
                while cur + 1 in hashSet:
                    cur += 1
                    length += 1
                result = max(result, length)
        return result
from typing import List, Set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result: int = 0
        hashSet: Set = set(nums)
        
        for num in nums:
            if num - 1 not in hashSet:
                length: int = 1
                cur: int = num
                while cur + 1 in hashSet:
                    cur += 1
                    length += 1
                result = max(result, length)
        return result
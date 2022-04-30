from typing import List, Set

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash: Set[int] = set()

        for num in nums:
            if num in hash:
                return num
            hash.add(num)
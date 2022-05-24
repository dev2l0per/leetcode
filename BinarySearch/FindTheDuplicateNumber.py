from typing import List, Set

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashMap: Set = set()

        for num in nums:
            if num in hashMap:
                return num
            hashMap.add(num)
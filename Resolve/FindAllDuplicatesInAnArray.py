from typing import List, Set

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashMap: Set = set()
        result: List[int] = []

        for num in nums:
            if num in hashMap:
                result.append(num)
            hashMap.add(num)
        return result
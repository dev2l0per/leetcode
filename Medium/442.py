from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashSet = set()
        result = []
        for num in nums:
            if num in hashSet:
                result.append(num)
            hashSet.add(num)
        return result
from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = Counter()
        result = []

        for num in nums1:
            hash[num] += 1
        for num in nums2:
            if num in hash and hash[num] != 0:
                result.append(num)
                hash[num] -= 1
        return result
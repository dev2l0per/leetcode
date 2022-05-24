from typing import List, Dict
from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap: Dict = defaultdict(int)
        result: List[int] = []

        for num in nums1:
            hashMap[num] += 1
        for num in nums2:
            if num in hashMap and hashMap[num] != 0:
                result.append(num)
                hashMap[num] -= 1
        return result
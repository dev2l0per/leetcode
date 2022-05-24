from typing import List, Dict
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashMap: Dict = defaultdict(int)
        result: int = 0

        for num1 in nums1:
            for num2 in nums2:
                hashMap[num1 + num2] += 1
        for num3 in nums3:
            for num4 in nums4:
                if -(num3 + num4) in hashMap:
                    result += hashMap[-(num3 + num4)]
        return result
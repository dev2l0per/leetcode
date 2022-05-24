from typing import List, Dict
from collections import defaultdict

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: List[int] = []
        
        for num in nums1:
            result.append(nums2.index(num))
        return result
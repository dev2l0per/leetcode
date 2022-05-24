from typing import List, Dict
from collections import defaultdict

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hashMap: Dict = defaultdict(int)
        result: int = 0

        for num in nums:
            hashMap[num] += 1
        for key, value in enumerate(hashMap):
            if key - k in hashMap:
                result = result + (hashMap[key - k] * value)
        return result
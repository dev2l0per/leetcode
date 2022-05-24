from typing import List, Dict
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap: Dict = defaultdict(int)
        result: int = 0

        hashMap[0] = 1
        save: int = 0
        for num in nums:
            save += num
            result += hashMap[save - k]
            hashMap[save] += 1
        return result
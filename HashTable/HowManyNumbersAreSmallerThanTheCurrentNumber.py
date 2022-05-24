from typing import List, Dict
from collections import defaultdict

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashMap: Dict = defaultdict(int)

        for i, v in enumerate(sorted(nums)):
            if v not in hashMap:
                hashMap[v] = i
        return [hashMap[num] for num in nums]
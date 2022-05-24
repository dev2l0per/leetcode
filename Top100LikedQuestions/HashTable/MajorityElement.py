from typing import List, Dict
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count: Dict = defaultdict(int)

        for num in nums:
            count[num] += 1
        sortedCount = sorted(count.items(), key=lambda x: (x[1], x[0]), reverse=True)

        return sortedCount[0][0]
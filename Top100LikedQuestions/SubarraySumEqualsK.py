from typing import List, Dict
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash: Dict = defaultdict(int)
        result: int = 0

        hash[0] = 1
        sum = 0

        for num in nums:
            sum += num
            result += hash[sum-k]
            hash[sum] += 1

        return result
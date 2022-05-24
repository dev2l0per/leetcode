from typing import List, Dict
import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap: List[int] = []
        hash: Dict = defaultdict(int)
        result: List[int] = []

        for num in nums:
            hash[num] += 1
        for num in hash:
            heapq.heappush(heap, (hash[num], num))
        while len(heap) > k:
            heapq.heappop(heap)
        for num in heap:
            result.append(num[1])
        return result
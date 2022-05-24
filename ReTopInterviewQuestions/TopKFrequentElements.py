from typing import List, Dict
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: Dict = Counter(nums)
        heap: List[int] = []
        result: List[int] = []

        for i in count:
            heapq.heappush(heap, (count[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        for i in heap:
            result.append(i[1])
        return result
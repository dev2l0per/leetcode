import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap: List[int] = []
        
        for row in matrix:
            for num in row:
                heapq.heappush(heap, num)
        result: int = 0
        for _ in range(k):
            result = heapq.heappop(heap)
        return result
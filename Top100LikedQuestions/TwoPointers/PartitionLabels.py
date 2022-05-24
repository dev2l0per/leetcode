from typing import List, Dict
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap: Dict = defaultdict(int)
        result: List[int] = []

        for i, v in enumerate(s):
            hashMap[v] = i
        start: int = 0
        cur: int = 0
        for i, v in enumerate(s):
            cur = max(cur, hashMap[v])
            if cur == i:
                result.append(cur - start + 1)
                start = cur + 1
        return result
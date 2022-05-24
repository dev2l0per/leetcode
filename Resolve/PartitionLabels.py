from typing import List, Dict
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap: Dict = defaultdict(int)
        result: List[int] = []

        for index, value in enumerate(s):
            hashMap[value] = index
        start: int = 0
        cursor: int = 0
        for index, value in enumerate(s):
            cursor = max(cursor, hashMap[value])
            if cursor == index:
                result.append(cursor - start + 1)
                start = cursor + 1
        return result
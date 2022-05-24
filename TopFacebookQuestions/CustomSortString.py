from typing import Dict, List
from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count: Dict = defaultdict(int)
        result: List[str] = []

        for ch in s:
            count[ch] += 1
        for ch in order:
            result.append(ch * count[ch])
            del count[ch]
        for ch in count:
            result.append(ch * count[ch])
        return ''.join(result)
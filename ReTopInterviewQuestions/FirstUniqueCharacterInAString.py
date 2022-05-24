from typing import Dict
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap: Dict = defaultdict(int)

        for ch in s:
            hashMap[ch] += 1
        for ch in hashMap:
            if hashMap[ch] == 1:
                return s.index(ch)
        return -1
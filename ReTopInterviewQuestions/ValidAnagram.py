from typing import Dict
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash: Dict = defaultdict(int)
        tHash: Dict = defaultdict(int)

        for ch in s:
            sHash[ch] += 1
        for ch in t:
            tHash[ch] += 1
        return sHash == tHash
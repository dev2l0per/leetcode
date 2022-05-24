from typing import List, Dict
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sLength: int = len(s)
        pLength: int = len(p)
        result: List[int] = []
        sCounter: Dict = defaultdict(int)
        pCounter: Dict = defaultdict(int)

        if sLength < pLength:
            return result

        for ch in p:
            pCounter[ch] += 1
        for i in range(pLength - 1):
            sCounter[s[i]] += 1
        
        left: int = 0
        right: int = pLength - 1

        while right < sLength:
            sCounter[s[right]] += 1
            while right - left >= pLength:
                sCounter[s[left]] -= 1
                if sCounter[s[left]] == 0:
                    del sCounter[s[left]]
                left += 1
            if sCounter == pCounter:
                result.append(left)
            right += 1
        return result
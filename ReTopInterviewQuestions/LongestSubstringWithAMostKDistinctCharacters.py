from typing import Dict
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hashMap: Dict = defaultdict(int)
        result: int = 0

        n: int = len(s)
        left: int = 0
        right: int = 0
        
        while right < n:
            hashMap[s[right]] = right

            if len(hashMap) > k:
                index = min(hashMap.values())
                left = index + 1
                del hashMap[s[index]]
            result = max(result, right - left + 1)
            right += 1
        return result
from typing import Dict
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hash: Dict = defaultdict(int)
        result: int = 0

        length: int = len(s)
        left: int = 0
        right: int = 0

        while right < length:
            hash[s[right]] = right

            if len(hash) > k:
                index = min(hash.values())
                left = index + 1
                del hash[s[index]]
            
            result = max(result, right - left + 1)
            right += 1
        return result
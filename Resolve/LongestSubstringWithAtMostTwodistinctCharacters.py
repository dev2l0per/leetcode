from typing import Dict
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        length: int = len(s)

        if length < 3:
            return length
        
        result: int = 0
        left: int = 0
        right: int = 0
        hash: Dict = defaultdict(int)

        while right < length:
            hash[s[right]] = right

            if len(hash) > 2:
                index = min(hash.values())
                left = index + 1
                del hash[s[index]]
            result = max(result, right - left + 1)
            right += 1
        return result
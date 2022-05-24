from typing import Dict
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left: int = 0
        result: int = 0
        hashMap: Dict = defaultdict(int)

        for right in range(len(s)):
            if s[right] in hashMap:
                left = max(left, hashMap[s[right]] + 1)
            hashMap[s[right]] = right
            result = max(result, right - left + 1)
        return result
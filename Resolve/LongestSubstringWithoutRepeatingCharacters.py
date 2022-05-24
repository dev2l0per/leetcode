from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash: Dict[str, int] = {}
        left: int = 0
        result: int = 0

        for right in range(len(s)):
            if s[right] in hash:
                left = max(hash[s[right]] + 1, left)
            hash[s[right]] = right
            result = max(result, right - left + 1)
        return result
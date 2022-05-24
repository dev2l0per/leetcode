class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or len(s) < k:
            return 0
        if k == 0:
            return len(s)
        i: int = 0
        while i < len(s):
            if s.count(s[i]) < k:
                break
            i += 1
        if len(s) == i:
            return i
        return max(self.longestSubstring(s[:i], k), self.longestSubstring(s[i + 1:], k))
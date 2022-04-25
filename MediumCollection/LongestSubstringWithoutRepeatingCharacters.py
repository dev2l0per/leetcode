class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = {}
        i = 0
        result = 0
        for j in range(len(s)):
            if s[j] in check:
                i = max(check[s[j]] + 1, i)
            check[s[j]] = j
            result = max(result, j - i + 1)
        return result
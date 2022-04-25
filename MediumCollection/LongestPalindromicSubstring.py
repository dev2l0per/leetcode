class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            i -= 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            if len(result) <= j - i - 1:
                result = s[i + 1:j]
        return result
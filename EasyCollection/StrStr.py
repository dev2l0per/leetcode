class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hayLen, needLen = len(haystack), len(needle)

        for i in range(hayLen - needLen + 1):
            if haystack[i] == needle[0]:
                if haystack[i:i+needLen] == needle:
                    return i
        return -1
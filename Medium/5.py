class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        dp = [[False] * len(s) for i in range(len(s))]
        res = ''
        for subLength in range(len(s) + 1):
            for subIndex in range(len(s) - subLength):
                if s[subIndex] == s[subIndex + subLength]:
                    if subLength <= 1 or dp[subIndex+1][subIndex+subLength-1]:
                        dp[subIndex][subIndex + subLength] = True
                        res = s[subIndex:subIndex+subLength + 1]
        return res
        


sol = Solution()
print(sol.longestPalindrome("cbbd"))
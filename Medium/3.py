class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        tempString = ''
        i = 0
        while i < len(s):
            if s[i] in tempString:
                tempString = tempString[tempString.index(s[i]) + 1:]
            tempString += s[i]
            result = max(len(tempString), result)
            i += 1
        return result

sol = Solution()
result = sol.lengthOfLongestSubstring("abcabcbb")
print(result)
result = sol.lengthOfLongestSubstring("bbbbb")
print(result)
result = sol.lengthOfLongestSubstring("pwwkew")
print(result)
result = sol.lengthOfLongestSubstring("aabaab!bb")
print(result)
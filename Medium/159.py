from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        length = len(s)

        if length < 3:
            return length
        
        result = 0
        left, right = 0, 0
        hash = defaultdict()
        while right < length:
            hash[s[right]] = right
            right += 1
            
            if len(hash) > 2:
                index = min(hash.values())
                left = index + 1
                del hash[s[index]]
            
            result = max(result, right - left)
        return result

sol = Solution()
print(sol.lengthOfLongestSubstringTwoDistinct("eceba"))
print(sol.lengthOfLongestSubstringTwoDistinct("ccaabbbb"))
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        length = len(s)

        if length < k:
            return length
        
        left, right = 0, 0
        hash = defaultdict()
        result = 0

        while right < length:
            hash[s[right]] = right
            right += 1

            if len(hash) > k:
                index = min(hash.values())
                left = index + 1
                del hash[s[index]]
            
            result = max(result, right - left)
        
        return result

sol = Solution()
print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))
print(sol.lengthOfLongestSubstringKDistinct("aa", 1))
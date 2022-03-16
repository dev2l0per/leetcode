from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slength, plength = len(s), len(p)
        sHash, pHash = Counter(), Counter(p)
        result = []

        for index in range(slength):
            sHash[s[index]] += 1

            if index >= plength - 1:
                if sHash == pHash:
                    result.append(index - plength + 1)
                if sHash[s[index - plength + 1]] == 1:
                    del sHash[s[index - plength + 1]]
                else:
                    sHash[s[index - plength + 1]] -= 1
        
        return result

sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))
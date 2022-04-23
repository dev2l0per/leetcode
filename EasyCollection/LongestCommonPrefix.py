from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hash = {}
        length = len(strs)
        result = ""

        for str in strs:
            for ch in str:
                if ch not in hash:
                    hash[ch] = 1
                else:
                    hash[ch] += 1
        for ch in hash:
            if hash[ch] != length:
                break
            result += ch
        return result
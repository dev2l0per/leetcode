class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}

        for ch in s:
            if ch in hash:
                hash[ch] += 1
            else:
                hash[ch] = 1
        for ch in hash:
            if hash[ch] == 1:
                return s.index(ch)
        return -1
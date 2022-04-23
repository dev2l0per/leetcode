class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash, tHash = {}, {}

        for ch in s:
            if ch in sHash:
                sHash[ch] += 1
            else:
                sHash[ch] = 1
        for ch in t:
            if ch in tHash:
                tHash[ch] += 1
            else:
                tHash[ch] = 1
        return sHash == tHash
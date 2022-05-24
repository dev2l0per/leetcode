from typing import List, Set

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashMap: Set = set()
        result: int = 0

        for ch in allowed:
            hashMap.add(ch)
        for word in words:
            check: bool = True
            for ch in word:
                if ch not in hashMap:
                    check = False
                    break
            if check:
                result += 1
        return result
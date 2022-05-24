from typing import Dict, Set

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashMap: Set = set()
        result: int = 0

        for jewel in jewels:
            hashMap.add(jewel)
        for stone in stones:
            if stone in hashMap:
                result += 1
        return result
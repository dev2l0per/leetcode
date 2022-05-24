from typing import Set

class Solution:
    def isHappy(self, n: int) -> bool:
        hashMap: Set = set()
        
        while n != 1 and n not in hashMap:
            hashMap.add(n)

            totalSum: int = 0
            while n > 0:
                temp: int = n % 10
                totalSum += temp ** 2
                n = n // 10
            n = totalSum
        return n == 1
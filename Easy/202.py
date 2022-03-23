class Solution:
    def isHappy(self, n: int) -> bool:
        cycleHash = set()

        while n != 1 and n not in cycleHash:
            cycleHash.add(n)
            total = 0
            while n > 0:
                n, modulation = divmod(n, 10)
                total += modulation ** 2
            n = total

        return n == 1

sol = Solution()
print(sol.isHappy(19))
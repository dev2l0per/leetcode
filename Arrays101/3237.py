from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                result += 1
        return result

sol = Solution()
print(sol.findNumbers([12, 345, 2, 6, 7896]))
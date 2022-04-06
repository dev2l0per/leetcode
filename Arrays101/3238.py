from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        cnt = 0

        for num in nums:
            if num == 1:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 0
        return max(result, cnt)

sol = Solution()
print(sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(sol.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
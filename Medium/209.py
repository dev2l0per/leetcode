from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        numLength = len(nums)
        left = sum = 0
        result = numLength + 1
        
        for right in range(numLength):
            sum += nums[right]

            while sum >= target:
                result = min(result, right - left + 1)
                sum -= nums[left]
                left += 1
        
        if result == numLength + 1:
            return 0

        return result

sol = Solution()
print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(sol.minSubArrayLen(4, [1, 4, 4]))
print(sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
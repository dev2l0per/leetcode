from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 0:
            return 0
        if length == 1:
            return nums[0]

        current, prev = 0, 0

        for index in range(length - 1):
            save = current
            current = max(prev + nums[index], current)
            prev = save
        
        startFromZero = current

        current, prev = 0, 0

        for index in range(1, length):
            save = current
            current = max(prev + nums[index], current)
            prev = save
        
        startFromOne = current

        print(startFromZero, startFromOne)

        return max(startFromZero, startFromOne)

sol = Solution()
print(sol.rob([2, 3, 2]))
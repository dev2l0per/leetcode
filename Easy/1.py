from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tables = {}
        for index in range(len(nums)):
            difference = target - nums[index]
            if difference in tables:
                return [index, tables[difference]]
            tables[nums[index]] = index

sol = Solution()
result = sol.twoSum([3, 2, 4], 6)
print(result)
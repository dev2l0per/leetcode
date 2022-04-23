from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 1
        for i in range(0, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[cur] = nums[i + 1]
                cur += 1
        return cur

sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        
        def backtrack(cur: int):
            if cur == length:
                result.append(nums[:])
            for index in range(cur, length):
                nums[cur], nums[index] = nums[index], nums[cur]
                backtrack(cur + 1)
                nums[cur], nums[index] = nums[index], nums[cur]
        
        result = []
        backtrack(0)

        return result

sol = Solution()
print(sol.permute([1, 2, 3]))
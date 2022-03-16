from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)

        nums.sort()

        def backtrack(index: int, arr: List[int]):
            result.append(list(arr))
            for i in range(index, length):
                if i != index and nums[i] == nums[i - 1]:
                    continue
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop(len(arr) - 1)

        backtrack(0, [])
        
        return result

sol = Solution()
print(sol.subsetsWithDup([4, 4, 4, 1, 4]))
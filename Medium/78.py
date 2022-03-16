from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        length = len(nums)

        def backtrack(index: int, arr: List[int]):
            if index == length:
                return
            arr.append(nums[index])
            result.append(list(arr))
            for i in range(index + 1, length + 1):
                backtrack(i, arr)
            arr.pop(len(arr) - 1)


        for i in range(length):
            backtrack(i, [])
        
        return result

sol = Solution()
print(sol.subsets([1, 2, 3]))
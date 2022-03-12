from typing import List


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         table = [[0] * len(nums)] * len(nums)
#         result = nums[0]

#         for i in range(len(nums)):
#             table[i][i] = nums[i]
#             if nums[i] > result:
#                 result = nums[i]
        
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 table[i][j] = table[i - 1][j] + table[i][i]
#                 if table[i][j] > result:
#                     result = table[i][j]
#         return result

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         for i in range(1, len(nums)):
#             nums[i] = nums[i] + (nums[i - 1] if nums[i - 1] > 0 else 0)
#         return max(nums)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        currentMax = nums[0]
        for i in range(1, len(nums)):
            currentMax = max(nums[i], currentMax + nums[i])
            result = max(currentMax, result)
        return result


sol = Solution()
print(sol.maxSubArray([5, 4, -1, 7, 8]))

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSum(nums, i, result)
        return result
    def twoSum(self, nums, index, res):
        hash = set()
        i = index + 1
        while i < len(nums):
            comp = -nums[index] - nums[i]
            if comp in hash:
                res.append([nums[index], nums[i], comp])
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
            hash.add(nums[i])
            i += 1
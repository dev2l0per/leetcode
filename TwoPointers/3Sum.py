from typing import List, Set

class Solution:
    def threeSum(self, nums: List[int]) -> List[int]:
        nums.sort()
        result: List[int] = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                hashMap: Set = set()
                j: int = i + 1
                while j < len(nums):
                    temp: int = -nums[i] - nums[j]
                    if temp in hashMap:
                        result.append([nums[i], nums[j], temp])
                        while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                            j +=1
                    hashMap.add(nums[j])
                    j += 1
        return result
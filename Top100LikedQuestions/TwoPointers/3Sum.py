from typing import List, Set, Dict

class Solution:
    def threeSum(self, nums: List[int]) -> List[int]:
        result: Set = set()
        dups: Set = set()
        seen: Dict = {}

        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i + 1:]):
                    temp: int = -val1 - val2
                    if temp in seen and seen[temp] == i:
                        result.add(tuple(sorted((val1, val2, temp))))
                    seen[val2] = i
        return result
        
        
        
        # nums.sort()
        # result: List[int] = []
        
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         break
        #     if i == 0 or nums[i] != nums[i - 1]:
        #         hashSet: Set = set()
        #         j: int = i + 1
        #         while j < len(nums):
        #             temp: int = -nums[i] - nums[j]
        #             if temp in hashSet:
        #                 result.append([nums[i], nums[j], temp])
        #                 while j + 1 < len(nums) and nums[j] == nums[j + 1]:
        #                     j += 1
        #             hashSet.add(nums[j])
        #             j += 1
        # return result




        # nums.sort()
        # result: List[int] = []

        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         break
        #     if i == 0 or nums[i] != nums[i - 1]:
        #         low: int = i + 1
        #         high: int = len(nums) - 1
        #         while low < high:
        #             sum: int = nums[i] + nums[low] + nums[high]
        #             if sum < 0:
        #                 low += 1
        #             elif sum > 0:
        #                 high -= 1
        #             else:
        #                 result.append([nums[i], nums[low], nums[high]])
        #                 low += 1
        #                 high -= 1
        #                 while low < high and nums[low] == nums[low - 1]:
        #                     low += 1
        # return result
from typing import List, Dict
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap: Dict = defaultdict(int)

        for i in range(len(nums)):
            temp: int = target - nums[i]
            if temp in hashMap:
                return [hashMap[temp], i]
            hashMap[nums[i]] = i
        
        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             return [i, j]
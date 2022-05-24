from typing import List, Dict
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result: int = 0
        hashMap: Dict = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] in hashMap:
                for index in hashMap[nums[i]]:
                    if index < i:
                        result += 1
            hashMap[nums[i]].append(i)
        return result
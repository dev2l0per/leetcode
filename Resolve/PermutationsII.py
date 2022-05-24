from typing import List, Counter
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        hash: Counter = Counter(nums)

        def backtrack(arr: List[int]) -> None:
            if len(arr) == len(nums):
                result.append(arr[:])
                return
            for num in hash:
                if hash[num] > 0:
                    arr.append(num)
                    hash[num] -= 1
                    backtrack(arr)
                    hash[num] += 1
                    arr.pop()
        backtrack([])
        return result
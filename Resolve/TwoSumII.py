from typing import List, Dict
from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hash: Dict = defaultdict(int)

        # for i in range(len(numbers)):
        #     if numbers[i] not in hash:
        #         hash[target - numbers[i]] = i
        #     else:
        #         return [hash[numbers[i]] + 1, i + 1]
        # return []
        l: int = 0
        r: int = len(numbers) - 1

        while l < r:
            temp: int = numbers[l] + numbers[r]

            if temp == target:
                return [l + 1, r + 1]
            elif temp > target:
                r -= 1
            else:
                l += 1
        return []
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        while index1 < index2:
            res = numbers[index1] + numbers[index2]
            
            if res == target:
                return [index1 + 1, index2 + 1]
            elif res < target:
                index1 = index1 + 1
            else:
                index2 = index2  - 1
        return [0, 0]
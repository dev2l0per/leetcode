from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hash = Counter()

        # for num in nums:
        #     hash[num] += 1
        # for num in hash:
        #     if hash[num] == 1:
        #         return num
        # return 0
        i = 0
        for num in nums:
            i ^= num
        return i
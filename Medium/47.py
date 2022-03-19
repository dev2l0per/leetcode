from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        numsHash = Counter(nums)

        def backtrack(arr: List[int], hash):
            if len(arr) == length:
                result.append(arr[:])
                return
            for num in hash:
                if hash[num] > 0:
                    arr.append(num)
                    hash[num] -= 1
                    backtrack(arr, hash)
                    hash[num] += 1
                    arr.pop()
        
        backtrack([], numsHash)
        return result

sol = Solution()
print(sol.permuteUnique([1, 1, 2]))
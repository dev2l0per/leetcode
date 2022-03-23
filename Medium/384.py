from typing import List
import random

class Solution:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.origins = nums[:]
        print(self.origins)

    def reset(self) -> List[int]:
        self.nums = self.origins[:]
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            randomIndex = random.randrange(0, len(self.nums))
            self.nums[i], self.nums[randomIndex] = self.nums[randomIndex], self.nums[i]
        
        return self.nums

sol = Solution([1, 2, 3])
sol.shuffle()
print(sol.origins)
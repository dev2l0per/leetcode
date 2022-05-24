from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryFlag: bool = True

        for i in range(len(digits) - 1, -1, -1):
            if carryFlag:
                if digits[i] == 9:
                    digits[i] = 0
                    carryFlag = True
                else:
                    digits[i] += 1
                    carryFlag = False
        if carryFlag:
            return [1] + digits
        return digits
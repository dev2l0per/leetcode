from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True

        for i in range(len(digits) - 1, -1, -1):
            if flag:
                if digits[i] == 9:
                    digits[i] = 0
                    flag = True
                else:
                    digits[i] += 1
                    flag = False
        if flag:
            return [1] + digits
        return digits
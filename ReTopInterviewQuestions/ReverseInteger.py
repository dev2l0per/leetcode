class Solution:
    def reverse(self, x: int) -> int:
        result: int = 0
        minusFlag: bool = False
        if x < 0:
            x *= -1
            minusFlag = True
        while x > 0:
            num: int = x % 10
            result = result * 10 + num
            x = x // 10
        if result > 2147483647:
            return 0
        return result if minusFlag == False else -result
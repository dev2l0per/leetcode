class Solution:
    def reverse(self, x: int) -> int:
        result: int = 0
        flag: bool = False
        if x < 0:
            x *= -1
            flag = True
        while x > 0:
            num: int = x % 10
            x = x // 10
            result = result * 10 + num
        if result > 2147483647:
            return 0
        if flag:
            return -result
        return result
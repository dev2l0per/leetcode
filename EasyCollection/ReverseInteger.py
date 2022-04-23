class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        result = 0
        if x < 0:
            x *= -1
            flag = True
        
        while x != 0:
            num = x % 10
            x = x // 10
            result = result * 10 + num
        
        if result > 2147483647:
            return 0

        if flag:
            return -result
        return result
class Solution:
    def reverse(self, x: int) -> int:
        result, flag = 0, False
        if x < 0:
            x *= -1
            flag = True
        while x > 0:
            digit = x % 10
            x = int(x / 10)
            result = result * 10 + digit
            if result > 2147483647:
                return 0
        return result if not flag else -result

sol = Solution()
print(sol.reverse(123))
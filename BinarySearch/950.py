class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x // 2

        if x == 1:
            return 1

        while left <= right:
            mid = (left + right) // 2

            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

sol = Solution()
print(sol.mySqrt(4))
print(sol.mySqrt(8))
print(sol.mySqrt(1))
print(sol.mySqrt(6))
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 2, num // 2

        if num < 3:
            return True

        while left <= right:
            mid = (left + right) // 2

            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

sol = Solution()
print(sol.isPerfectSquare(14))
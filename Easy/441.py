class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2
            cur = mid * (mid + 1) // 2
            if cur == n:
                return mid
            if n < cur:
                right = mid - 1
            else:
                left = mid + 1
        return right
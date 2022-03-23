class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left < right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt

sol = Solution()
print(sol.rangeBitwiseAnd(11, 15))
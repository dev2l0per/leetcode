class Solution:
    def mySqrt(self, x: int) -> int:
        l: int = 0
        r: int = x

        while l <= r:
            mid: int = (l + r) // 2

            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                l = mid +1
            else:
                r = mid -1
        return r
class Solution:
    def mySqrt(self, x: int) -> int:
        left: int = 0
        right: int = x

        while left <= right:
            mid: int = (left + right) // 2

            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
        
        # i: int = 1

        # while i * i <= x:
        #     i += 1
        # return i - 1
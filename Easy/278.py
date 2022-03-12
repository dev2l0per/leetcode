class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            middle = int((left + right) / 2)

            if isBadVersion(middle) == False:
                left = middle + 1
            else:
                right = middle
        return right
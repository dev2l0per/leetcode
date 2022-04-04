from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        result = 0
        for num1 in arr1:
            left, right = 0, len(arr2)
            while left < right:
                mid = (left + right) // 2
                if abs(arr2[mid] - num1) <= d:
                    result -= 1
                    break
                elif arr2[mid] > num1:
                    right = mid
                else:
                    left = mid + 1
            result += 1
        return result
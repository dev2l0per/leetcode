from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left: int, right: int, pivotIndex: int) -> int:
            pivot: int = nums[pivotIndex]
            nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
            storeIndex: int = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[storeIndex], nums[i] = nums[i], nums[storeIndex]
                    storeIndex += 1
            nums[right], nums[storeIndex] = nums[storeIndex], nums[right]
            return storeIndex
        def select(left: int, right: int, kSmallest: int) -> int:
            if left == right:
                return nums[left]
            pivotIndex: int = random.randint(left, right)
            pivotIndex = partition(left, right, pivotIndex)
            if kSmallest == pivotIndex:
                return nums[kSmallest]
            elif kSmallest < pivotIndex:
                return select(left, pivotIndex - 1, kSmallest)
            return select(pivotIndex + 1, right, kSmallest)
        return select(0, len(nums) - 1, len(nums) - k)
        
        # pivot: int = (len(nums) - 1) // 2

        # left: List[int] = []
        # mid: List[int] = []
        # right: List[int] = []

        # for num in nums:
        #     if nums[pivot] == num:
        #         mid.append(num)
        #     elif nums[pivot] > num:
        #         left.append(num)
        #     else:
        #         right.append(num)
        # if len(right) >= k:
        #     return self.findKthLargest(right, k)
        # elif len(right) + len(mid) >= k:
        #     return mid[0]
        # else:
        #     return self.findKthLargest(left, k - (len(right) + len(mid)))
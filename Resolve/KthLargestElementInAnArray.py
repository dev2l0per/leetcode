from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot: int = (len(nums) - 1) // 2

        left: List[int] = []
        mid: List[int] = []
        right: List[int] = []

        for num in nums:
            if nums[pivot] == num:
                mid.append(num)
            elif nums[pivot] > num:
                left.append(num)
            else:
                right.append(num)
        print(left)
        print(mid)
        print(right)
        print(k)
        if len(right) >= k:
            return self.findKthLargest(right, k)
        elif len(right) + len(mid) >= k:
            return mid[0]
        else:
            return self.findKthLargest(left, k - (len(mid) + len(right)))
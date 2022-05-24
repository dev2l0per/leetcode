from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        length: int = len(nums)
        k %= length

        for i in range(k):
            if i >= k // 2:
                break
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]
        for i in range(k, length):
            if i >= (length + k) // 2:
                break
            nums[i], nums[length - 1 - (i - k)] = nums[length - 1 - (i - k)], nums[i]
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        n: int = len(nums)
        k = k % n

        for i in range(k):
            if i >= k // 2:
                break
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]
        for i in range(k, n):
            if i >= (n + k) // 2:
                break
            nums[i], nums[n - 1 - (i - k)] = nums[n - 1 - (i - k)], nums[i]
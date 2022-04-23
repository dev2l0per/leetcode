from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k %= l

        start = cnt = 0

        while cnt < l:
            current, prev = start, nums[start]
            while True:
                nextIdx = (current + k) % l
                nums[nextIdx], prev = prev, nums[nextIdx]
                current = nextIdx
                cnt += 1
                
                if start == current:
                    break
            start += 1
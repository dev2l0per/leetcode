from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur1: int = m - 1
        cur2: int = n - 1

        for i in range(len(nums1) - 1, -1, -1):
            if cur1 < 0:
                nums1[i] = nums2[cur2]
                cur2 -= 1
            elif cur2 < 0:
                nums1[i] = nums1[cur1]
                cur1 -= 1
            else:
                if nums1[cur1] < nums2[cur2]:
                    nums1[i] = nums2[cur2]
                    cur2 -= 1
                else:
                    nums1[i] = nums1[cur1]
                    cur1 -= 1
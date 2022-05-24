from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            mid: int = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        
        # def binarySearch(left: int, right: int) -> int:
        #     if left > right:
        #         return -1
        #     mid: int = (left + right) // 2

        #     if nums[mid] == target:
        #         return mid
        #     if nums[left] <= nums[mid]:
        #         if nums[left] <= target and target <= nums[mid]:
        #             return binarySearch(left, mid - 1)
        #         return binarySearch(mid + 1, right)
        #     if nums[mid] <= target and target <= nums[right]:
        #         return binarySearch(mid + 1, right)
        #     return binarySearch(left, mid - 1)
        # return binarySearch(0, len(nums) - 1)
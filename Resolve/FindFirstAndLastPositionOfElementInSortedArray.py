from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l: int = 0
        r: int = len(nums) - 1
        upper: int = -1
        lower: int = -1

        while l <= r:
            mid: int = (l + r) // 2
            
            if nums[mid] == target:
                if mid == l or nums[mid - 1] < target:
                    upper = mid
                    break
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if upper == -1:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid: int = (l + r) // 2
            if nums[mid] == target:
                if mid == r or nums[mid + 1] > target:
                    lower = mid
                    break
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return [upper, lower]

sol = Solution()
sol.searchRange(nums = [5,7,7,8,8,10], target = 11)
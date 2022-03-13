from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        l = len(nums)
        if l < 3:
            return result
        
        nums.sort()
        for cur in range(l - 2):
            if nums[cur] > 0:
                break
            if cur != 0 and nums[cur - 1] == nums[cur]:
                continue
            left, right = cur + 1, l - 1
            while left < right:
                num = nums[cur] + nums[left] + nums[right]
                if num == 0:
                    result.append([nums[cur], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                elif num < 0:
                    left += 1
                else:
                    right -= 1
        
        return result

sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
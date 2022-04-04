from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[int], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left < right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        if left == len(letters) - 1 and letters[left] <= target:
            return letters[0]
        return letters[left]

sol = Solution()
print(sol.nextGreatestLetter(["c", "f", "j"], "a"))
print(sol.nextGreatestLetter(["c", "f", "j"], "c"))
print(sol.nextGreatestLetter(["c", "f", "j"], "d"))
print(sol.nextGreatestLetter(["c", "f", "j"], "j"))
print(sol.nextGreatestLetter(["c", "f", "j"], "k"))
print(sol.nextGreatestLetter(["c", "f", "j"], "g"))
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result: List[List[str]] = []

        def isPalindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(arr: List[str], startIndex):
            if startIndex >= len(s):
                result.append(arr[:])
                return
            for i in range(startIndex, len(s)):
                if isPalindrome(startIndex, i):
                    arr.append(s[startIndex:i+1])
                    backtrack(arr, i + 1)
                    arr.pop()
        backtrack([], 0)
        return result
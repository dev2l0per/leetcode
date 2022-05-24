from typing import Dict, List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letters: Dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result: List[str] = []

        def backtrack(arr: List[int], startIndex: int) -> None:
            if len(digits) == len(arr):
                result.append(''.join(arr))
                return
            for ch in letters[digits[startIndex]]:
                arr.append(ch)
                backtrack(arr, startIndex + 1)
                arr.pop()
        backtrack([], 0)
        return result
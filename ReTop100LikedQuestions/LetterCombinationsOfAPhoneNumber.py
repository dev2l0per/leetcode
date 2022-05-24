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

        result: List[int] = []

        def backtrack(arr: List[int], index: int) -> None:
            if len(arr) == len(digits):
                result.append(''.join(arr))
                return
            for ch in letters[digits[index]]:
                arr.append(ch)
                backtrack(arr, index + 1)
                arr.pop()
        backtrack([], 0)
        return result
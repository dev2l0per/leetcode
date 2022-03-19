from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def backtrack(combination: List[str], index):
            if len(combination) == len(digits):
                result.append("".join(combination))
                return
            for letter in letters[digits[index]]:
                combination.append(letter)
                backtrack(combination, index + 1)
                combination.pop()
        
        backtrack([], 0)
        return result

sol = Solution()
print(sol.letterCombinations("23"))
print(sol.letterCombinations(""))
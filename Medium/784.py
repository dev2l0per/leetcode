from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result: List[str] = []

        for element in s:
            resultLength = len(result)
            if element.isalpha():
                if resultLength == 0:
                    result.append(element.lower())
                    result.append(element.upper())
                else:
                    for index in range(resultLength):
                        result.append(result[index] + element.upper())
                        result[index] += element.lower()
            else:
                if resultLength == 0:
                    result.append(element)
                else:
                    for index in range(len(result)):
                        result[index] += element
        
        return result

sol = Solution()
print(sol.letterCasePermutation("3z4"))
print(sol.letterCasePermutation("a1b2"))
print(sol.letterCasePermutation("C"))
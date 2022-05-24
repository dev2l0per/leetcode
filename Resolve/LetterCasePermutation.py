from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result: List[str] = []

        for ch in s:
            curResultLength: int = len(result)
            if ch.isalpha():
                if curResultLength == 0:
                    result.append(ch.lower())
                    result.append(ch.upper())
                else:
                    for i in range(curResultLength):
                        result.append(result[i] + ch.lower())
                        result[i] += ch.upper()
            else:
                if curResultLength == 0:
                    result.append(ch)
                else:
                    for i in range(curResultLength):
                        result[i] += ch
        return result



# class Solution:
#     def letterCasePermutation(self, s: str) -> List[str]:
#         result: List[str] = []

#         def backtrack(arr: List[str], index: int) -> None:
#             if len(arr) == len(s):
#                 result.append(''.join(arr))
#                 return
#             if s[index].isalpha():
#                 arr.append(s[index].lower())
#                 backtrack(arr, index + 1)
#                 arr.pop()
#                 arr.append(s[index].upper())
#                 backtrack(arr, index + 1)
#                 arr.pop()
#             else:
#                 arr.append(s[index])
#                 backtrack(arr, index + 1)
#                 arr.pop()
#         backtrack([], 0)
#         return result
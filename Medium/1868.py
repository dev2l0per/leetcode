from typing import List

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        cursor1 = cursor2 = 0
        result = []

        while cursor1 < len(encoded1) and cursor2 < len(encoded2):
            cnt = min(encoded1[cursor1][1], encoded2[cursor2][1])

            encoded1[cursor1][1] -= cnt
            encoded2[cursor2][1] -= cnt
            product = encoded1[cursor1][0] * encoded2[cursor2][0]

            if encoded1[cursor1][1] == 0:
                cursor1 += 1
            if encoded2[cursor2][1] == 0:
                cursor2 += 1
            
            if result and result[-1][0] == product:
                result[-1][1] += cnt
            else:
                result.append([product, cnt])
        
        return result
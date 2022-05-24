from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []
        
        firstLength: int = len(firstList)
        secondLength: int = len(secondList)

        firstCur: int = 0
        secondCur: int = 0
        while firstCur < firstLength and secondCur < secondLength:
            startTime: int = max(firstList[firstCur][0], secondList[secondCur][0])
            endTime: int = min(firstList[firstCur][1], secondList[secondCur][1])

            if startTime <= endTime:
                result.append([startTime, endTime])
            if firstList[firstCur][1] < secondList[secondCur][1]:
                firstCur += 1
            else:
                secondCur += 1
        return result
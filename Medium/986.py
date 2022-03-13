from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []

        firstCur, secondCur = 0, 0

        while firstCur < len(firstList) and secondCur < len(secondList):
            startInterval = max(firstList[firstCur][0], secondList[secondCur][0])
            endInterval = min(firstList[firstCur][1], secondList[secondCur][1])

            if startInterval <= endInterval:
                result.append([startInterval, endInterval])

            if firstList[firstCur][1] < secondList[secondCur][1]:
                firstCur += 1
            else:
                secondCur += 1
        return result

sol = Solution()
print(sol.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))
print(sol.intervalIntersection(firstList = [[1,3],[5,9]], secondList = []))
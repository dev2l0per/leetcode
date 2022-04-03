from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        cursor1, cursor2 = 0, 0

        slots1.sort()
        slots2.sort()

        while cursor1 < len(slots1) and cursor2 < len(slots2):
            startTime = max(slots1[cursor1][0], slots2[cursor2][0])

            if startTime + duration > slots1[cursor1][1]:
                cursor1 += 1
            elif startTime + duration > slots2[cursor2][1]:
                cursor2 += 1
            else:
                return [startTime, startTime + duration]
        return []

sol = Solution()
print(sol.minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8))
print(sol.minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12))
print(sol.minAvailableDuration([[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]]
,[[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]]
,456085))
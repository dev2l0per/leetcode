from typing import List

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        colorHash = {
            1: [],
            2: [],
            3: [],
        }
        result = []

        for index, color in enumerate(colors):
            colorHash[color].append(index)

        for queryIndex, queryColor in queries:
            if len(colorHash[queryColor]) == 0:
                result.append(-1)
            elif colors[queryIndex] == queryColor:
                result.append(0)
            else:
                left, right = 0, len(colorHash[queryColor]) - 1

                while left < right:
                    mid = int((left + right) / 2)

                    if colorHash[queryColor][mid] < queryIndex:
                        left = mid + 1
                    else:
                        right = mid
                
                if left == len(colorHash[queryColor]):
                    result.append(abs(colorHash[queryColor][left - 1] - queryIndex))
                elif left == 0:
                    result.append(abs(colorHash[queryColor][left] - queryIndex))
                else:
                    minRes = min(abs(colorHash[queryColor][left] - queryIndex), abs(colorHash[queryColor][left - 1] - queryIndex))
                    result.append(minRes)
        return result

sol = Solution()
print(sol.shortestDistanceColor(colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]))
print(sol.shortestDistanceColor(colors = [1,2], queries = [[0,3]]))
print(sol.shortestDistanceColor([2,1,2,2,1], [[1,1],[4,3],[1,3],[4,2],[2,1]]))
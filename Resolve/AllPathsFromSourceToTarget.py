from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []
        n: int = len(graph)

        def backtrack(arr: List[int], cur: int):
            if cur == n - 1:
                result.append(arr[:])
                return
            for nextCur in graph[cur]:
                arr.append(nextCur)
                backtrack(arr, nextCur)
                arr.pop()
        backtrack([0], 0)
        return result
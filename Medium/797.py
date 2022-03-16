from typing import List
from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        target = len(graph) - 1
        stack = deque([0])

        def backtrack(cur):
            if cur == target:
                result.append(list(stack))
            for next in graph[cur]:
                stack.append(next)
                backtrack(next)
                stack.pop()
        
        backtrack(0)

        return result
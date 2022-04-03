from operator import ne
from typing import List
from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        adjList = defaultdict(list)
        visit = [False for _ in range(n)]
        result = 0

        for connection in connections:
            adjList[connection[0]].append(connection[1])
            adjList[connection[1]].append(connection[0])

        def dfs(index):
            if visit[index]:
                return
            visit[index] = True
            for next in adjList[index]:
                dfs(next)
            return
        
        for i in range(n):
            if not visit[i]:
                dfs(i)
                result += 1
        return result - 1

sol = Solution()
# print(sol.makeConnected(4, [[0,1],[0,2],[1,2]]))
print(sol.makeConnected(11,[[1,4],[0,3],[1,3],[3,7],[2,7],[0,1],[2,4],[3,6],[5,6],[6,7],[4,7],[0,7],[5,7]]))
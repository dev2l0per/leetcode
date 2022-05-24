from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n: int = len(isConnected)
        visited: List[bool] = [False] * n
        result: int = 0

        def dfs(index: int) -> None:
            for i in range(n):
                if isConnected[index][i] == 1 and visited[i] == False:
                    visited[i] = True
                    dfs(i)

        for i in range(n):
            if visited[i] == False:
                dfs(i)
                result += 1
        return result
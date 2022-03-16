from typing import List
from collections import deque

# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         length = len(isConnected)
#         queue = deque()
#         visited = [False] * length
#         result = 0

#         for i in range(length):
#             if visited[i] == False:
#                 queue.append(i)

#                 while queue:
#                     cur = queue.popleft()
#                     visited[cur] = True

#                     for j in range(length):
#                         if isConnected[cur][j] == 1 and visited[j] == False:
#                             queue.append(j)
                
#                 result += 1
        
#         return result

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        length = len(isConnected)
        visited = [False] * length
        result = 0

        def dfs(i):
            for j in range(length):
                if isConnected[i][j] == 1 and visited[j] == False:
                    visited[j] = True
                    dfs(j)
        
        for i in range(length):
            if visited[i] == False:
                dfs(i)
                result += 1
        
        return result

sol = Solution()
print(sol.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(sol.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
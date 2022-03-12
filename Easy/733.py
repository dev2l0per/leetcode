from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        bfsQueue = deque()
        visited = [[False] * n for _ in range(m)]
        direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        visited[sr][sc] = True
        bfsQueue.append([sr, sc])

        while bfsQueue:
            cur = bfsQueue.popleft()
            for curDirection in direction:
                if cur[0] + curDirection[0] < 0 or cur[0] + curDirection[0] >= m or cur[1] + curDirection[1] < 0 or cur[1] + curDirection[1] >= n:
                    continue
                if image[cur[0]][cur[1]] == image[cur[0] + curDirection[0]][cur[1] + curDirection[1]] and visited[cur[0] + curDirection[0]][cur[1] + curDirection[1]] == False:
                    bfsQueue.append([cur[0] + curDirection[0], cur[1] + curDirection[1]])
                    visited[cur[0] + curDirection[0]][cur[1] + curDirection[1]] = True
            image[cur[0]][cur[1]] = newColor
        
        return image


sol = Solution()
print(sol.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
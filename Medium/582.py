from typing import List
from collections import defaultdict, deque

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        table = defaultdict(list)
        result = []

        for ppidNum in range(len(ppid)):
            if ppid[ppidNum] == 0:
                continue
            table[ppid[ppidNum]].append(pid[ppidNum])
        
        queue = deque()
        queue.append(kill)

        while queue:
            cur = queue.popleft()
            result.append(cur)

            if cur not in table:
                continue
            for child in table[cur]:
                queue.append(child)
        return result

sol = Solution()
print(sol.killProcess(pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5))
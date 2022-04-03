from typing import List
from collections import deque

class Solution:
    def openLock(self, depends: List[str], target: str) -> int:
        queue = deque()
        check = set()

        queue.append(('0000', 0))
        check.add('0000')

        while queue:
            cur, cnt = queue.popleft()

            if cur == target:
                return cnt
            if cur in depends:
                continue
            for i in range(4):
                for t in (-1, 1):
                    change = int(cur[i]) + t
                    if change < 0:
                        change = 9
                    elif change > 9:
                        change = 0
                    newCollection = cur[:i] + str(change) + cur[i + 1:]
                    if newCollection not in check:
                        check.add(newCollection)
                        queue.append((newCollection, cnt + 1))
        return -1
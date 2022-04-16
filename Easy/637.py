from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        waitQueue = deque()
        nextQueue = deque()

        nextQueue.append(root)
        while nextQueue:
            # 복사 => Count 해서 하는 방향으로 Extra Queue 없이도 가능할 듯
            while nextQueue:
                waitQueue.append(nextQueue.popleft())
            length = len(waitQueue)
            sum = 0
            while waitQueue:
                cur = waitQueue.popleft()
                sum += cur.val
                if cur.left:
                    nextQueue.append(cur.left)
                if cur.right:
                    nextQueue.append(cur.right)
            result.append(sum / length)
        return result
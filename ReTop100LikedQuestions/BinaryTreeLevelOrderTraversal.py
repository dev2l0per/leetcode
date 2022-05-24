from typing import Optional, List, Deque
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []

        if root is None:
            return result

        queue: Deque = deque()
        queue.append((root, 0))

        while queue:
            queueLen: int = len(queue)
            result.append([])
            for _ in range(queueLen):
                cur: TreeNode
                level: int
                cur, level = queue.popleft()
                result[level].append(cur.val)
                if cur.left:
                    queue.append((cur.left, level + 1))
                if cur.right:
                    queue.append((cur.right, level + 1))
        return result
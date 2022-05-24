from typing import Optional, List, Deque
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result: List[int] = []
        queue: Deque = deque()

        queue.append(root)
        while queue:
            result.append(queue[-1].val)
            cnt: int = len(queue)
            for _ in range(cnt):
                cur: TreeNode = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result
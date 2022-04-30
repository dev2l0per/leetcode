from typing import Optional, Deque, Tuple
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue: Deque[Tuple[Optional[TreeNode], int]] = deque()
        result: int = 0
        queue.append((root, 0))

        while queue:
            cur: Tuple[Optional[TreeNode], int] = queue.popleft()

            if cur[0].left is None and cur[0].right is None:
                result = max(result, cur[1] + 1)
            if cur[0].left:
                queue.append((cur[0].left, cur[1] + 1))
            if cur[0].right:
                queue.append((cur[0].right, cur[1] + 1))
        return result
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque()

        queue.append((0, root))
        while queue:
            cur = queue.popleft()

            if cur[1].left is None and cur[1].right is None:
                return cur[0] + 1
            if cur[1].left:
                queue.append((cur[0] + 1, cur[1].left))
            if cur[1].right:
                queue.append((cur[0] + 1, cur[1].right))
        return 0
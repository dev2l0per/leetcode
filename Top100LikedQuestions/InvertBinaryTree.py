from typing import Optional, Deque
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        queue: Deque[Optional[TreeNode]] = deque()
        queue.append(root)

        while queue:
            cur: Optional[TreeNode] = queue.popleft()
            cur.left, cur.right = cur.right, cur.left

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root
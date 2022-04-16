from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = deque()
        result = 0

        stack.append((root, 0))
        while stack:
            cur = stack.pop()

            if cur[0].left is None and cur[0].right is None:
                result = max(result, cur[1] + 1)
            if cur[0].left:
                stack.append((cur[0].left, cur[1] + 1))
            if cur[0].right:
                stack.append((cur[0].right, cur[1] + 1))
        return result
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        stack = deque()

        stack.append((root, root.val))
        while stack:
            cur = stack.pop()

            if cur[0].left is None and cur[0].right is None and cur[1] == targetSum:
                    return True
            if cur[0].left:
                stack.append((cur[0].left, cur[1] + cur[0].left.val))
            if cur[0].right:    
                stack.append((cur[0].right, cur[1] + cur[0].right.val))
        return False
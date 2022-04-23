from typing import Optional
from collections import deque
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, min, max):
            if root is None:
                return True
            if root.val <= min:
                return False
            if root.val >= max:
                return False
            return validate(root.left, min, root.val) & validate(root.right, root.val, max)
        return validate(root, -math.inf, math.inf)
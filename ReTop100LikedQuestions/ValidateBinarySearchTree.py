from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: TreeNode, max: int, min: int) -> bool:
            if node is None:
                return True
            if node.val <= min:
                return False
            if node.val >= max:
                return False
            return validate(node.left, node.val, min) and validate(node.right, max, node.val)
        return validate(root, math.inf, -math.inf)
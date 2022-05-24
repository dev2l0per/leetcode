from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result: int = 0

        def traversal(node: TreeNode) -> None:
            if node is None:
                return
            traversal(node.left)
            if low <= node.val and node.val <= high:
                self.result += node.val
            traversal(node.right)
        traversal(root)
        return self.result
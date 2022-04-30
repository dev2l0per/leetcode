from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traversal(node: Optional[TreeNode]) -> TreeNode:
            if node is None:
                return None
            if node.left is None and node.right is None:
                return node
            
            leftSubTree: TreeNode = traversal(node.left)
            rightSubTree: TreeNode = traversal(node.right)

            if leftSubTree:
                leftSubTree.right = node.right
                node.right = node.left
                node.left = None
            if rightSubTree:
                return rightSubTree
            return leftSubTree
        traversal(root)
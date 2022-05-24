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
        Do not return anything, modify root in-place instaed.
        """

        def dfs(node: TreeNode) -> TreeNode:
            if node is None:
                return
            if node.left is None and node.right is None:
                return node
            
            leftTree: TreeNode = dfs(node.left)
            rightTree: TreeNode = dfs(node.right)

            if leftTree:
                leftTree.right = node.right
                node.right = node.left
                node.left = None
            if rightTree:
                return rightTree
            return leftTree
        dfs(root)
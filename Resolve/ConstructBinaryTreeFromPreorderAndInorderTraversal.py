from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            rootIndex: int = inorder.index(preorder.pop(0))

            root: TreeNode = TreeNode(inorder[rootIndex])
            root.left = self.buildTree(preorder, inorder[0: rootIndex])
            root.right = self.buildTree(preorder, inorder[rootIndex + 1:])
            return root
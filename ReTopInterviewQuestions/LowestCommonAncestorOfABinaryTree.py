# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        if root == p or root == q:
            return root
        left: TreeNode = self.lowestCommonAncestor(root.left, p, q)
        right: TreeNode = self.lowestCommonAncestor(root.right, p, q)

        if left is None:
            return right
        if right is None:
            return left
        return root
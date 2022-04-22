# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def backtrack(node: 'TreeNode'):
            if node is None:
                return False
            
            left = backtrack(node.left)
            right = backtrack(node.right)

            mid = node == p or node == q

            if mid + left + right >= 2:
                self.ans = node
            return mid or left or right
        backtrack(root)
        return self.ans
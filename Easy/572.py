from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val:
            if self.checkSubtree(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) | self.isSubtree(root.right, subRoot)
    
    def checkSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
        return self.checkSubtree(root.left, subRoot.left) & self.checkSubtree(root.right, subRoot.right)

a = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(5))), TreeNode(5))
b = TreeNode(4, TreeNode(1), TreeNode(2))
c = TreeNode(1, TreeNode(1))
d = TreeNode(1)

sol = Solution()
print(sol.isSubtree(c, d))
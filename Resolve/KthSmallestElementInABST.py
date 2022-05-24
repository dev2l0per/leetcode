from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal: List[int] = []

        def inOrderTraversal(node: TreeNode) -> None:
            if node is None:
                return
            inOrderTraversal(node.left)
            traversal.append(node.val)
            inOrderTraversal(node.right)
        inOrderTraversal(root)
        return traversal[k-1]
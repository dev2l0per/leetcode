from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def preOrderTraversal(node: Optional[TreeNode], depth):
            if node is None:
                return
            if len(result) == depth:
                result.append([])
            result[depth].append(node.val)
            if node.left:
                preOrderTraversal(node.left, depth + 1)
            if node.right:
                preOrderTraversal(node.right, depth + 1)
        
        preOrderTraversal(root, 0)
        return result
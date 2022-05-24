from typing import Optional, List

# Definition for a singly-linked node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result: List[List[int]] = []

        def preOrderTraversal(node: TreeNode, sum: int, arr: List[int]) -> None:
            if node is None:
                return
            if sum + node.val == targetSum and node.left is None and node.right is None:
                result.append(arr[:] + [node.val])
                return
            preOrderTraversal(node.left, sum + node.val, arr + [node.val])
            preOrderTraversal(node.right, sum + node.val, arr + [node.val])
        preOrderTraversal(root, 0, [])
        return result
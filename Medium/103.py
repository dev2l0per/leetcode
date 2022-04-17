from collections import deque
from typing import Deque, Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[Deque] = []

        def preOrderTraversal(node, depth):
            if node is None:
                return
            if len(result) == depth:
                result.append(deque())
            if depth % 2 == 0:
                result[depth].append(node.val)
            else:
                result[depth].appendleft(node.val)
            if node.left:
                preOrderTraversal(node.left, depth + 1)
            if node.right:
                preOrderTraversal(node.right, depth + 1)
        
        preOrderTraversal(root, 0)
        return result
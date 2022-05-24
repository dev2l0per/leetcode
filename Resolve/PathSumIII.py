from typing import Optional, Dict
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hash: Dict[int, int] = defaultdict(int)
        self.count: int = 0

        def traversal(node: TreeNode, curSum: int) -> None:
            if node is None:
                return
            curSum += node.val
            if curSum == targetSum:
                self.count += 1
            self.count += hash[curSum - targetSum]
            hash[curSum] += 1
            traversal(node.left, curSum)
            traversal(node.right, curSum)
            hash[curSum] -= 1
        traversal(root, 0)
        return self.count
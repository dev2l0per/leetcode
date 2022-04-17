from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hashMap = defaultdict(int)
        self.count = 0

        def preOrderTraserval(node: Optional[TreeNode], curSum):
            if node is None:
                return
            curSum += node.val
            if curSum == targetSum:
                self.count += 1
            self.count += hashMap[curSum - targetSum]
            hashMap[curSum] += 1
            preOrderTraserval(node.left, curSum)
            preOrderTraserval(node.right, curSum)
            hashMap[curSum] -= 1
        
        preOrderTraserval(root, 0)
        return self.count
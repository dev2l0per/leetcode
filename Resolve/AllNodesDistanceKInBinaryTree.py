from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result: List[int] = []

        if k == 0:
            return [target.val]

        def dfs(node: TreeNode, currentK: int) -> int:
            if node is None:
                return -1
            if currentK == k:
                result.append(node.val)
                return -1
            if node.val == target.val or currentK > 0:
                leftK: int = dfs(node.left, currentK + 1)
                rightK: int = dfs(node.right, currentK + 1)
                if currentK == 0:
                    return 1
            else:
                leftK: int = dfs(node.left, currentK)
                rightK: int = dfs(node.right, currentK)
            if leftK == k or rightK == k:
                result.append(node.val)
                return -1
            if leftK > 0:
                dfs(node.right, leftK + 1)
                return leftK + 1
            if rightK > 0:
                dfs(node.left, rightK + 1)
                return rightK + 1
            return 0
        dfs(root, 0)
        return result
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, path, arr, tempSum):
            if node is None:
                return
            path.append(node)
            arr.append(node.val)
            tempSum += node.val
            if tempSum == targetSum and node.left is None and node.right is None:
                result.append(arr[:])
            else:
                if node.left:
                    dfs(node.left, path[:], arr[:], tempSum)
                if node.right:
                    dfs(node.right, path[:], arr[:], tempSum)
        
        dfs(root, [], [], 0)
        return result
from typing import Optional, List, Deque, Tuple
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []
        if root is None:
            return result
        queue: Deque[Tuple(TreeNode, int)] = deque()

        queue.append((root, 0))
        while queue:
            queueLength: int = len(queue)
            result.append([])
            for _ in range(queueLength):
                cur: Tuple(TreeNode, int) = queue.popleft()
                result[cur[1]].append(cur[0].val)
                if cur[0].left:
                    queue.append((cur[0].left, cur[1] + 1))
                if cur[0].right:
                    queue.append((cur[0].right, cur[1] + 1))
        return result
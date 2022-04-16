from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()

        queue.append((p, q))
        while queue:
            cur = queue.popleft()

            if cur[0] is None or cur[1] is None:
                if not (cur[0] is None and cur[1] is None):
                    return False
            else:
                if cur[0].val != cur[1].val:
                    return False
            if cur[0] and cur[1]:
                queue.append((cur[0].left, cur[1].left))
                queue.append((cur[0].right, cur[1].right))
        return True